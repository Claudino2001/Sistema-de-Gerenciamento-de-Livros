# Dockerfile para Books Service
FROM python:3.8-slim
WORKDIR /app
COPY books_service.py /app
RUN pip install Flask Flask-JWT-Extended
CMD ["python", "books_service.py"]
