import base64
import openai
import streamlit as st
import urllib.request
from PIL import Image
import os


# Function to add app background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(f"""<style>.stApp {{background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
    background-size: cover}}</style>""", unsafe_allow_html=True)


# Function to generate images with rate limiting
def generate_image(prompt, api_key):
    """Gera imagem usando DALL-E com tratamento de erros"""
    try:
        # Configura a API key
        openai.api_key = api_key
        
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
    except Exception as e:
        st.error(f"Erro ao gerar imagem: {str(e)}")
        return None


# Streamlit app
st.markdown("""
    <svg width="600" height="100">
        <text x="50%" y="50%" font-family="monospace" font-size="42px" fill="grey" text-anchor="middle" stroke="black"
         stroke-width="0.5" stroke-linejoin="round">Fotomontagem
        </text>
    </svg>
""", unsafe_allow_html=True)

add_bg_from_local('background.jpg')

# Configuração segura da API key
def get_openai_api_key():
    """Obtém a API key do OpenAI de forma segura"""
    # Primeiro tenta obter dos secrets do Streamlit
    try:
        return st.secrets["OPENAI_API_KEY"]
    except KeyError:
        # Se não estiver nos secrets, tenta variável de ambiente
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            return api_key
        else:
            # Fallback para input do usuário (apenas para desenvolvimento)
            return st.sidebar.text_input("OpenAI API Key:", type="password", help="Configure OPENAI_API_KEY nos secrets do Streamlit para produção")

# Obtém a API key
api_key = get_openai_api_key()

img_description = st.text_input('Descrição da Imagem:', placeholder="Descreva a imagem que deseja gerar...")

if st.button('Gerar Imagem', use_container_width=True):
    if not api_key:
        st.warning("⚠️ Configure a OPENAI_API_KEY nos secrets do Streamlit ou nas variáveis de ambiente")
    elif not img_description.strip():
        st.warning("⚠️ Digite uma descrição para a imagem")
    else:
        with st.spinner('Gerando imagem...'):
            response = generate_image(img_description.strip(), api_key)
            if response:
                st.image(response, caption=img_description, use_column_width=True)
                st.success("✅ Imagem gerada com sucesso!")