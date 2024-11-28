# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Configurar o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o diretório de trabalho
COPY . .

# Expor a porta 888 (onde o Flask irá rodar)
EXPOSE 8888

# Comando para executar a aplicação
CMD ["python", "app.py"]
