FROM python:3

EXPOSE 8888

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "server.py"]
