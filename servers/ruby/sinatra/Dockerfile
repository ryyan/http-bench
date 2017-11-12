FROM ruby:alpine

EXPOSE 8888

WORKDIR /app
COPY . .

RUN gem install sinatra sinatra-contrib

CMD ["ruby", "server.rb"]
