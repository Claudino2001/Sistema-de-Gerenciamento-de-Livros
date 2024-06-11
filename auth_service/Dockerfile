# Dockerfile para Auth Service
FROM python:3.8-slim
WORKDIR /app
COPY auth_service.py /app
RUN pip install Flask Flask-JWT-Extended
CMD ["python", "auth_service.py"]
