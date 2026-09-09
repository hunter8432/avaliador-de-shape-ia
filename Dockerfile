#Esse codigo é pra rodar a linguagem que eu quero 
FROM python:3.10-slim 
#Aqui é onde vai ficar armazenado dentro do linux
WORKDIR /app 
#esse codigo vai copiar todos os arquivos 
COPY . /app 
#pra instalar as bibliotecas necessarios 
RUN pip install --no-cache-dir streamlit pandas pillow google-genai python-dotenv
#pra expor a porta, padrao do steamlit
EXPOSE 8501 
#sempre que o docker inciar vai inicializar junto tudo isso
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
