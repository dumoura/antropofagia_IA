import base64
import openai
import streamlit as st
import urllib.request
from PIL import Image


# Function to add app background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(f"""<style>.stApp {{background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
    background-size: cover}}</style>""", unsafe_allow_html=True)


# Function to generate images with rate limiting
def generate_image(prompt):
    img_response = openai.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="256x256",
        quality="hd",
        n=1,
    )
    
    image_url = img_response.data[0].url
    urllib.request.urlretrieve(image_url, 'img.png')
    img = Image.open("img.png")

    return img


# Streamlit app
st.markdown("""
    <svg width="600" height="100">
        <text x="50%" y="50%" font-family="monospace" font-size="42px" fill="grey" text-anchor="middle" stroke="black"
         stroke-width="0.5" stroke-linejoin="round">Fotomontagem
        </text>
    </svg>
""", unsafe_allow_html=True)

add_bg_from_local('background.jpg')

# Entering OpenAI API key
openai.api_key = st.sidebar.text_input("First, enter your OpenAI API key : ", type="password")

img_description = st.text_input('Image Description : ')

if st.button('Generate Image'):
    if openai.api_key:
        if img_description:
            try:
                with st.spinner('Generating Image...'):
                    response = generate_image(img_description)
                    st.image(response, caption=img_description, use_column_width=True)
            except Exception as e:
                st.error("Please enter valid OpenAI API key.")
    else:
        st.warning("Please input your OpenAI API key.")