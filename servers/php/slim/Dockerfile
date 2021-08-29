#FROM richarvey/nginx-php-fpm:1.10.4
FROM php:8-fpm

EXPOSE 8888

WORKDIR /app
COPY . .

COPY --from=composer:2 /usr/bin/composer /usr/local/bin/composer

RUN composer install
CMD [ "composer", "start" ]