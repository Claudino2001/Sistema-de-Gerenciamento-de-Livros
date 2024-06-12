# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos requirements.txt e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que a aplicação vai usar (para fins de documentação)
EXPOSE 5002

# Defina o comando para rodar a aplicação com Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5002", "books_service:app"]

