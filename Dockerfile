FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r backend/requirements.txt
CMD ["python","backend/main.py"]
