FROM openjdk:16-buster

EXPOSE 8888

WORKDIR /app
COPY . .

# Install Gradle
ENV GRADLE_VERSION 7.2
RUN wget -q https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip \
    && unzip gradle-$GRADLE_VERSION-bin.zip -d /opt \
    && rm gradle-$GRADLE_VERSION-bin.zip
ENV GRADLE_HOME /opt/gradle-$GRADLE_VERSION
ENV PATH $PATH:/opt/gradle-$GRADLE_VERSION/bin

RUN gradle build

CMD ["gradle", "run"]
