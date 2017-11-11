# Host Info
```
10 Nov 2017

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

# Benchmarks

## go/go

```
go version go1.9 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   469.83us    0.89ms  21.07ms   95.40%
    Req/Sec    33.16k     1.51k   36.72k    65.45%
  362949 requests in 11.00s, 54.69MB read
Requests/sec:  32994.97
Transfer/sec:      4.97MB
```
## node/express

```
v8.6.0
express@ /app
+-- express@4.16.2 
`-- uuid@3.1.0 

```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.53ms  746.09us  12.31ms   92.61%
    Req/Sec     4.42k   564.52     4.92k    88.18%
  48327 requests in 11.00s, 12.08MB read
Requests/sec:   4393.16
Transfer/sec:      1.10MB
```
