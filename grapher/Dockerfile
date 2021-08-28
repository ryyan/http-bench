FROM python:3

WORKDIR /app
COPY . .

RUN apt-get update \
    && apt-get install -fy libxft-dev libfreetype6 libfreetype6-dev \
    && pip install matplotlib

CMD ["python", "graph.py"]
