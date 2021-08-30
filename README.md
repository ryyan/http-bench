# http-bench

Benchmarks http servers

[View the latest results in RESULTS.md](RESULTS.md)

![Results graph](RESULTS.png?raw=true)

## Setup

Install [Docker](https://www.docker.com)

## Run

Use `./run <action> <server>` to run individual servers and benchmarks

```bash
./run list              # List servers
./run build go/go       # Build docker image
./run start go/go       # Run in daemon mode
./run start-int go/go   # Run in interactive mode
./run start-dev go/go   # Run in development mode
./run info go/go        # Run info script
./run test              # Run happy/error path tests
./run benchmark         # Run benchmark
./run stop go/go        # Stop daemon
./run clean go/go       # Delete docker image
```

Example script to run a single test case

```bash
./run build go/go
./run start go/go
./run test
./run benchmark
./run stop go/go
```

Use `./run-benchmarks` to run the full suite of benchmarks and output to RESULTS.md

```bash
./run-benchmarks
```

(Optional) Clear up disk space :whale:

```bash
docker system prune
```

## Servers

Each server must:

- Include a `Dockerfile` with a CMD

- Include an `info` executable that will be used to get relevant language version and package info

- Listen on port 8888 and have an "/echo/" endpoint
  - "/echo/" endpoint expects "HelloWorld" path parameter and "?num=1234567890" query parameter
  - Happy Path request: `localhost:8888/echo/HelloWorld?num=1234567890`
  - Error Path request: `localhost:8888/echo/AlohaWorld?num=321`

- Perform the following on each request:
  - Log request, for example [Date IP Method Url]:
    - `2017/11/11 11:11:12 [::1]:36942 GET /echo/HelloWorld?num=1234567890`
  - Parse out the path (words) and query string (num) parameters
  - Verify the parameters
    - Path parameter after "/echo" must be To-Lowercased and equal "helloworld"
    - Query parameter "num" must be converted to an int and equal 1234567890
  - If either parameter is invalid (error path), return
    - Status: `400 Bad Request`
    - Body: `{"error": "Invalid parameters"}`
  - If both are valid (happy path), return
    - Status: `200 OK`
    - Body: `{"message": "random UUID v4"}`
