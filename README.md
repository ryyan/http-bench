# http-bench

Benchmarks http servers

[View the latest results](RESULTS.md)

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

Use `./run-benchmarks` to run the full suite of benchmarks and output to RESULTS.md

```bash
./run-benchmarks
```

(Optional) Clear up disk space :whale:

```bash
docker system prune
```

## Servers

Each server must satisfy the following requirements

- Include a `Dockerfile` with a CMD

- Include an `info` executable that will be used to get relevant language version and package info

- Listen on port 8888 and have an "/api/echo/" endpoint
  - "/api/echo/" endpoint expects "HelloWorld" path parameter and "?num=1234567890" query parameter
  - `localhost:8888/api/echo/HelloWorld?num=1234567890`

- Return a json response
  - Happy path:
    - Status: `200 OK`
    - Response: `{"message": "random UUID v4"}`
  - Error path:
    - Status: `400 Bad Request`
    - Response: `{"error": "Invalid parameters"}`

- Perform the following on each request:
  - Log request, for example [Date IP Method Url]:
    - `2017/11/11 11:11:12 [::1]:36942 GET /api/echo/HelloWorld?num=1234567890`
  - Parse out the path and query string parameters
  - Verify the parameters
    - Path parameter after "/api/echo" must be To-Lowercased and equal "helloworld"
    - Query parameter "num" must be converted to an int and equal 1234567890
    - Return Error path response if invalid
  - Return Happy path response

- Be human readable and consistent across languages/frameworks - this benchmark prioritizes "average usage" over "maximum performance"
