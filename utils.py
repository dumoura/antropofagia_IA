from pathlib import Path
import openai

import streamlit as st
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI

from dotenv import load_dotenv, find_dotenv
import os

from configs import *

# Carrega variáveis de ambiente de forma segura
_ = load_dotenv(find_dotenv())

# Validação de variáveis de ambiente obrigatórias
def validate_environment():
    """Valida se as variáveis de ambiente necessárias estão definidas"""
    required_vars = ['OPENAI_API_KEY']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise EnvironmentError(f"Variáveis de ambiente obrigatórias não encontradas: {', '.join(missing_vars)}")
    
    return True


PASTA_ARQUIVOS = Path(__file__).parent / 'arquivos'


def importacao_documentos():
    documentos = []
    for arquivo in PASTA_ARQUIVOS.glob('*.pdf'):
        loader = PyPDFLoader(str(arquivo))
        documentos_arquivo = loader.load()
        documentos.extend(documentos_arquivo)
    return documentos

def split_de_documentos(documentos):
    recur_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2500,
        chunk_overlap=250,
        separators=["/n\n", "\n", ".", " ", ""]
    )
    documentos = recur_splitter.split_documents(documentos)

    for i, doc in enumerate(documentos):
        doc.metadata['source'] = doc.metadata['source'].split('/')[-1]
        doc.metadata['doc_id'] = i
    return documentos

def cria_vector_store(documentos):
    embedding_model = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(
        documents=documentos,
        embedding=embedding_model
    )
    return vector_store

def cria_chain_conversa():
    """Cria a cadeia de conversação com validação de ambiente"""
    try:
        # Valida variáveis de ambiente antes de prosseguir
        validate_environment()
        
        documentos = importacao_documentos()
        if not documentos:
            raise ValueError("Nenhum documento encontrado para processar")
            
        documentos = split_de_documentos(documentos)
        vector_store = cria_vector_store(documentos)

        chat = ChatOpenAI(model=get_config('model_name'))
        memory = ConversationBufferMemory(
            return_messages=True,
            memory_key='chat_history',
            output_key='answer'
            )
        retriever = vector_store.as_retriever(
            search_type=get_config('retrieval_search_type'),
            search_kwargs=get_config('retrieval_kwargs')
        )
        prompt = PromptTemplate.from_template(get_config('prompt'))
        chat_chain = ConversationalRetrievalChain.from_llm(
            llm=chat,
            memory=memory,
            retriever=retriever,
            return_source_documents=True,
            verbose=True,
            combine_docs_chain_kwargs={'prompt': prompt}
        )

        st.session_state['chain'] = chat_chain
        return True
        
    except Exception as e:
        st.error(f"Erro ao criar cadeia de conversação: {str(e)}")
        return False
