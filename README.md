# http-bench

Benchmarks http servers

## Run

Use run.sh to run individual servers and benchmarks

```bash
./run.sh build go/go  # Builds docker image
./run.sh start go/go  # Run daemon
./run.sh benchmark    # Run benchmark
./run.sh stop go/go   # Stop daemon
./run.sh clean go/go  # Deletes docker image
```

Use benchmark.sh to run the full suite of benchmarks and output to RESULTS.md

```bash
./benchmark.sh
```

(Optional) Clear up disk space :whale:

```bash
docker system prune
```

## Servers

Each server must satisfy the following requirements

- Listen on port 8888 and have an "/api/echo/" endpoint
  - "/api/echo/" endpoint expects "HelloWorld" path parameter and "?num=1234567890" query parameter
  - localhost:8888/api/echo/HelloWorld?num=1234567890

- Return a json response with "Content-Type" of "application/json"
  - Happy path:
    - Status: 200 OK
    - Response: {"message": "random UUID v4"}
  - Error path:
    - Status: 400 Bad Request
    - Response: {"error": "Invalid parameters"}

- Perform the following on each request:
  1. Log request, for example:
    - 2017/11/11 11:11:12 [::1]:36942 GET /api/echo/HelloWorld?num=1234567890
  2. Parse out the path and query string parameters
  3. Verify the parameters
    - Path parameter after "/api/echo" must be To-Lowercased and equal "helloworld"
    - Query parameter "num" must be converted to an int and equal 1234567890
    - Return Error path response if invalid
  4. Return Happy path response
