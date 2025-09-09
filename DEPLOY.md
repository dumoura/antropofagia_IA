# 🚀 Guia de Deploy - Antropofagia IA

## Deploy no Streamlit Cloud

### 1. Preparação do Repositório

1. **Faça fork deste repositório** ou clone para seu GitHub
2. **Certifique-se de que todos os arquivos estão commitados**:
   ```bash
   git add .
   git commit -m "Preparação para deploy no Streamlit Cloud"
   git push origin main
   ```

### 2. Configuração no Streamlit Cloud

1. **Acesse [share.streamlit.io](https://share.streamlit.io/)**
2. **Clique em "New app"**
3. **Configure o repositório**:
   - Repository: `seu-usuario/antropofagia-ia`
   - Branch: `main`
   - Main file path: `RemixandoIAs.py`

### 3. Configuração de Secrets

1. **No painel do Streamlit Cloud, vá em "Settings" > "Secrets"**
2. **Adicione a seguinte configuração**:
   ```toml
   OPENAI_API_KEY = "sk-sua-chave-aqui"
   ```

### 4. Deploy

1. **Clique em "Deploy!"**
2. **Aguarde o build completar** (pode levar alguns minutos)
3. **Seu app estará disponível em**: `https://seu-app-name.streamlit.app`

## Configuração Local para Desenvolvimento

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/antropofagia-ia.git
cd antropofagia-ia
```

### 2. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as Variáveis de Ambiente
```bash
# Crie um arquivo .env
echo "OPENAI_API_KEY=sua-chave-aqui" > .env
```

### 4. Execute Localmente
```bash
streamlit run RemixandoIAs.py
```

## Estrutura de Arquivos para Deploy

```
antropofagia_IA/
├── .streamlit/
│   ├── config.toml          # Configuração local
│   ├── cloud.toml           # Configuração para produção
│   ├── secrets.toml         # Secrets locais (não commitado)
│   └── secrets.example.toml # Exemplo de secrets
├── .github/
│   └── workflows/
│       └── streamlit-deploy.yml # CI/CD
├── pages/                   # Páginas do Streamlit
├── arquivos/               # PDFs carregados pelos usuários
├── RemixandoIAs.py         # App principal
├── streamlit_app.py        # Fallback para Streamlit Cloud
├── utils.py                # Utilitários
├── configs.py              # Configurações
├── requirements.txt        # Dependências
├── .gitignore             # Arquivos ignorados
└── README.md              # Documentação
```

## Troubleshooting

### Erro: "OPENAI_API_KEY not found"
- Verifique se a chave está configurada nos secrets do Streamlit Cloud
- Para desenvolvimento local, verifique se o arquivo `.env` existe

### Erro: "No PDFs found"
- Certifique-se de que o usuário carregou arquivos PDF
- Verifique se a pasta `arquivos/` existe e tem permissões de escrita

### Erro de Dependências
- Verifique se todas as dependências estão no `requirements.txt`
- Execute `pip install -r requirements.txt` localmente

### App não carrega
- Verifique os logs no Streamlit Cloud
- Certifique-se de que o arquivo principal está correto
- Verifique se não há erros de sintaxe no código

## Segurança

✅ **Implementado**:
- API keys protegidas via Streamlit Secrets
- Validação de entrada de dados
- Tratamento robusto de erros
- Arquivos sensíveis no .gitignore
- Configurações de segurança no Streamlit

## Suporte

Para dúvidas ou problemas:
1. Verifique os logs do Streamlit Cloud
2. Consulte a documentação do [Streamlit](https://docs.streamlit.io/)
3. Abra uma issue no repositório
