FROM golang:alpine

EXPOSE 8888

WORKDIR /go/src/app
COPY . .

RUN apk add --update git
RUN go get -d -v ./...
RUN go install -v ./...

CMD ["app"]
