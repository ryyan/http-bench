FROM openjdk:16-jdk-slim

EXPOSE 8888

WORKDIR /app
COPY . .

RUN apt update \
    && apt install -fy maven \
    && mvn clean install

CMD ["mvn", "exec:java"]
