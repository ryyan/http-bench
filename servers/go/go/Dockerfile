FROM golang:alpine

EXPOSE 8888

WORKDIR /go/src/app
COPY . .

RUN apk add --update git
RUN go-wrapper download
RUN go-wrapper install

CMD ["go-wrapper", "run"]
