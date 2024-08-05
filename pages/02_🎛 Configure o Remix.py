import streamlit as st
from configs import get_config

from configs import get_config
from utils import PASTA_ARQUIVOS, cria_chain_conversa

import json


def config_page():
    st.header("👯‍♂️ Configurção de Remix 👯", divider=True)
    
    model_name = st.text_input("Modifique o modelo LLM", value=get_config("model_name"))
    retrieval_search_type = st.text_input("Modifique a busca pelos seus textos", value=get_config("retrieval_search_type"))
    retrieval_kargs = st.text_input("Modifique os parâmetros de busca pelos seus textos", value=json.dumps(get_config("retrieval_kwargs")))
    prompt = st.text_area("Modifique o prompt de sistema", height=350, value=get_config("prompt"))
    
    if st.button('Ajustar parâmetros de remix', use_container_width=True):
        st.session_state['model_name '] = model_name 
        st.session_state['retrieval_search_type'] = retrieval_search_type
        st.session_state['retrieval_kwargs'] =  json.loads(retrieval_kargs.replace("'", '"'))
        st.session_state['prompt'] = prompt
        
        st.rerun()
        
    if st.button('Atualizar ChatBot', use_container_width=True):
        if len(list(PASTA_ARQUIVOS.glob('*.pdf'))) == 0:
            st.error('Adicione arquivos .pdf para inicializar o chatbot')
        else:
            st.success('Inicializando o ChatBot...')
            cria_chain_conversa()
            st.rerun()
            
config_page()