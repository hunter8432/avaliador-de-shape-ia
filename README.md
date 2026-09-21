# 💪 Avaliador de Shape com Inteligência Artificial

Aplicação web desenvolvida em **Python + Streamlit** que utiliza a **API do Google Gemini** para analisar visualmente uma foto de um físico e gerar um relatório estruturado sobre desenvolvimento muscular, proporções, pontos fortes, oportunidades de melhoria e sugestões gerais de treino e estratégia corporal.

> **Importante:** as avaliações são baseadas apenas no conteúdo visual da imagem. Estimativas de percentual de gordura não são medições clínicas e não substituem avaliação profissional.

## 🚀 Funcionalidades

- Upload de imagens em JPG, JPEG e PNG
- Otimização automática da imagem antes do envio à IA
- Análise visual utilizando Google Gemini
- Relatório estruturado em Markdown
- Estimativa visual de percentual de gordura
- Análise de proporções e desenvolvimento muscular observável
- Identificação de pontos fortes e oportunidades de melhoria
- Sugestões gerais de foco de treino e estratégia corporal
- Tratamento de erros da API, incluindo limites de requisição (429) e indisponibilidade (503)
- Execução local ou através de Docker

## 🛠️ Tecnologias

- **Python 3.10**
- **Streamlit** — interface web
- **Pillow** — processamento e otimização de imagens
- **Google GenAI** — integração com Gemini
- **python-dotenv** — gerenciamento da variável de ambiente da API
- **Docker** — containerização da aplicação

## 📁 Estrutura do projeto

```text
avaliador-de-shape-ia/
│
├── main.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
│
├── config/
│   └── settings.py
│
├── components/
│   ├── api_key_input.py
│   ├── image_uploads.py
│   └── resultado.py
│
├── services/
│   ├── image_services.py
│   └── gemini_services.py
│
└── prompt/
    └── shape_prompt.py
```

### Responsabilidade de cada camada

**`main.py`**  
Orquestra o fluxo principal da aplicação.

**`config/`**  
Centraliza configurações e carregamento da chave da API.

**`components/`**  
Contém os componentes responsáveis pela interface do Streamlit.

**`services/`**  
Contém a lógica de processamento da imagem e comunicação com o Gemini.

**`prompt/`**  
Centraliza o prompt utilizado na análise.

Essa organização mantém a interface, a lógica de negócio, as configurações e o prompt separados, facilitando manutenção e evolução do projeto.

## 🔑 Configuração da API

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_aqui
```

A chave é carregada através do `python-dotenv`.

**Nunca publique sua chave da API no GitHub.**

## ▶️ Executando localmente

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/hunter8432/avaliador-de-shape-ia.git
cd avaliador-de-shape-ia
```

Crie e ative um ambiente virtual, se desejar:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
streamlit run main.py
```

A aplicação será disponibilizada pelo Streamlit, normalmente em:

```text
http://localhost:8501
```

## 🐳 Executando com Docker

Construa a imagem:

```bash
docker build -t avaliador-shape .
```

Execute o container:

```bash
docker run --rm -p 8501:8501 --env-file .env avaliador-shape
```

Depois acesse:

```text
http://localhost:8501
```

A API Key é fornecida ao container em tempo de execução através do arquivo `.env`, em vez de ser armazenada na imagem Docker.

## ⚠️ Limites da API

A aplicação depende da disponibilidade e da cota da API do Google Gemini. Quando a API retorna erros como **429 (limite de requisições)** ou **503 (indisponibilidade/sobrecarga)**, a aplicação apresenta uma mensagem amigável ao usuário.

## 🎯 Objetivo do projeto

O projeto foi desenvolvido como uma aplicação prática para estudar e demonstrar conceitos de:

- Python
- desenvolvimento web com Streamlit
- integração com APIs de inteligência artificial
- organização e separação de responsabilidades
- processamento de imagens
- gerenciamento de variáveis de ambiente
- tratamento de erros
- Docker e containerização

## 📌 Próximos passos

Possíveis evoluções do projeto:

- histórico de análises
- comparação entre avaliações
- autenticação de usuários
- armazenamento de resultados
- interface mais completa
- testes automatizados
- melhorias no prompt e na consistência das análises

## 📄 Licença

Este projeto é destinado a fins de estudo e portfólio.
