# Antropofagia digital

**Antropofagia digital** is part of an ongoing project (IA na Literatura e na Arte) that explores the convergence of artificial intelligence (AI), literature, and visual arts within the context of education and New Literacies. This initiative primarily focuses on the works of Murilo Mendes and Jorge de Lima, two pivotal figures in Brazilian modernist literature and art.

# IA na Literatura e na Arte (Generative AI, Literary and Art Education)

## Project Description

**IA na Literatura e na Arte** is an ongoing project exploring the convergence of artificial intelligence (AI), literature, and visual arts within education and New Literacies. This initiative primarily focuses on the works of Murilo Mendes and Jorge de Lima, two pivotal figures in Brazilian modernist literature and art.

### Objectives

- **Investigate AI's Role:** Examine how AI can enhance the study and appreciation of literature and visual arts.
- **Modernist Literature Focus:** Delve into the contributions of Murilo Mendes and Jorge de Lima.
- **Aesthetics of Remix and Photomontage:** Emphasize the creative potential of remixing and photomontage techniques through AI-assisted artistic creation and analysis.

### Inspiration

The project draws inspiration from a recent Museum of Modern Art (MAM) exhibition, aiming to reimagine literature study by incorporating modern technological advancements.

### Key Themes

1. **AI in Education:** Explore how AI can be integrated into educational practices to enrich literary and artistic studies.
2. **Literary Analysis:** Utilize AI to analyze and reinterpret the works of Mendes and de Lima.
3. **Artistic Creation:** Employ AI tools to create new forms of artistic expression inspired by modernist aesthetics.

## 🚀 Deploy no Streamlit Cloud

### Pré-requisitos
- Conta no [Streamlit Cloud](https://share.streamlit.io/)
- Repositório no GitHub com o código
- Chave da API do OpenAI

### Passos para Deploy

1. **Fork ou clone este repositório**
   ```bash
   git clone https://github.com/seu-usuario/antropofagia-ia.git
   cd antropofagia-ia
   ```

2. **Configure as variáveis de ambiente**
   - Acesse seu app no Streamlit Cloud
   - Vá em Settings > Secrets
   - Adicione:
     ```toml
     OPENAI_API_KEY = "sua-api-key-aqui"
     ```

3. **Deploy**
   - Conecte seu repositório ao Streamlit Cloud
   - Selecione o branch principal
   - O app será deployado automaticamente

### 🔧 Configuração Local

1. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure as variáveis de ambiente**
   ```bash
   # Crie um arquivo .env
   echo "OPENAI_API_KEY=sua-api-key-aqui" > .env
   ```

3. **Execute localmente**
   ```bash
   streamlit run RemixandoIAs.py
   ```

### 🛡️ Segurança

- ✅ API keys protegidas via Streamlit Secrets
- ✅ Validação de entrada de dados
- ✅ Tratamento robusto de erros
- ✅ Arquivos sensíveis no .gitignore

### 📁 Estrutura do Projeto

```
antropofagia_IA/
├── .streamlit/           # Configurações do Streamlit
│   ├── config.toml      # Configuração local
│   ├── cloud.toml       # Configuração para produção
│   └── secrets.toml     # Secrets (não commitado)
├── pages/               # Páginas do Streamlit
├── arquivos/            # PDFs carregados pelos usuários
├── RemixandoIAs.py      # App principal
├── utils.py             # Utilitários e funções
├── configs.py           # Configurações
└── requirements.txt     # Dependências
```

### Get Involved

We welcome contributions and collaborations from individuals interested in AI, literature, visual arts, and education. Join us in exploring the intersection between technology and the humanities.

For more information and to contribute, please visit our [Repository](https://remixdumoura.com/2023/12/14/multimodalidade-o-artista-em-panico-ia-na-literatura-e-na-arte/).
