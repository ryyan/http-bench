10 Nov 2017, 16:32

```
Linux 4.13.0-16-generic

Client:
 Version:      1.13.1
 API version:  1.26
 Go version:   go1.8.3
 Git commit:   092cba3
 Built:        Thu Oct 12 22:34:44 2017
 OS/Arch:      linux/amd64

Server:
 Version:      1.13.1
 API version:  1.26 (minimum version 1.12)
 Go version:   go1.8.3
 Git commit:   092cba3
 Built:        Thu Oct 12 22:34:44 2017
 OS/Arch:      linux/amd64
 Experimental: false
```

---

## go/go

```
go version go1.9 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 10s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   599.76us    1.39ms  24.09ms   94.35%
    Req/Sec    16.05k     1.58k   31.55k    84.58%
  320957 requests in 10.10s, 48.36MB read
Requests/sec:  31780.24
Transfer/sec:      4.79MB
```

---

## node/express

```
v8.6.0
express@ /app
+-- express@4.16.2 
`-- uuid@3.1.0 

```

```
HappyTest-PASS, ErrorTest-PASS
Running 10s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.29ms  728.99us  12.08ms   92.83%
    Req/Sec     2.23k   308.46     2.58k    85.00%
  44347 requests in 10.00s, 11.08MB read
Requests/sec:   4433.04
Transfer/sec:      1.11MB
```
