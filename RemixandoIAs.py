#streamlit run RemixandoIAs.py --server.enableXsrfProtection false
import streamlit as st 
import time
from utils import cria_chain_conversa, PASTA_ARQUIVOS


def sidebar():
    uploaded_pdfs = st.file_uploader(
        'Adicione poemas a sua coleção', type=['.pdf'], 
        accept_multiple_files=True
        )
    if not uploaded_pdfs is None:
        for arquivo in PASTA_ARQUIVOS.glob('*.pdf'):
            arquivo.unlink()
        for pdf in uploaded_pdfs:
        
            with open(PASTA_ARQUIVOS / pdf.name, 'wb') as f:
                f.write(pdf.read())

    label_botao = 'Incializar Chatbot'
    if 'chain' in st.session_state:
        label_botao = 'Atualizar ChatBot'
    if st.button(label_botao, use_container_width=True):
        if len(list( PASTA_ARQUIVOS.glob('*.pdf'))) == 0:
            st.error('Adicione arquivos .pdf a sua coleção para inicializar o ChatBot')
        else:
            st.success('Inicializando o Chatbot...')
            cria_chain_conversa()
            st.rerun()
            

def chat_window():
    st.header('👩🏾‍💻 Antropofagia digital: Remixando IAs 👩🏾‍💻', divider=True)
    
    if not 'chain' in st.session_state:
        st.error('Alimente seu bot com poemas em .pdf para iniciar!')
        st.stop()
        
    chain = st.session_state['chain']
    memory = chain.memory
    
    mensagens = memory.load_memory_variables({})['chat_history']
    
    container = st.container()
    for mensagem in mensagens:
        chat = container.chat_message(mensagem.type)
        chat.markdown(mensagem.content)
        
    nova_mensagem = st.chat_input('Remix sua coleção...')
    
    if nova_mensagem:
        chat = container.chat_message('human')
        chat.markdown(nova_mensagem)
        
        chat = container.chat_message('ai')
        chat.markdown('Remixando...')
        
        resposta = chain.invoke({"question": nova_mensagem})
        st.session_state['ultima_resposta'] = resposta
        st.rerun()
        
    
def main():
    with st.sidebar:
        sidebar()
    chat_window()
    

if __name__ == '__main__':
    main()