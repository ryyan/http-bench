FROM ruby:3

EXPOSE 8888

WORKDIR /app
COPY . .

RUN gem install sinatra sinatra-contrib puma

CMD ["ruby", "server.rb"]
