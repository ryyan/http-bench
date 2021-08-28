FROM richarvey/nginx-php-fpm:latest

EXPOSE 8888

WORKDIR /app
COPY . .
COPY site.conf /etc/nginx/sites-available/default.conf

RUN composer install
