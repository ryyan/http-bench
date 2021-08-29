FROM node:16

EXPOSE 8888

WORKDIR /app
COPY . .

ENV NODE_ENV production

RUN npm install

CMD ["npm", "start"]
