# Arquivo principal para o Streamlit Cloud
# Este arquivo é usado quando o Streamlit Cloud não encontra RemixandoIAs.py

import streamlit as st
import sys
import os

# Adiciona o diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importa e executa o app principal
from RemixandoIAs import main

if __name__ == "__main__":
    main()
