FROM rust:1

EXPOSE 8888

WORKDIR /app
COPY . .

RUN cargo build --release

CMD ["./target/release/server"]
