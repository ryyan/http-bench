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
Running 2m test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  20 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.96ms    1.91ms  44.03ms   84.26%
    Req/Sec     1.02k    93.53     3.37k    84.06%
  2439587 requests in 2.00m, 367.60MB read
Requests/sec:  20318.82
Transfer/sec:      3.06MB
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
Running 2m test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  20 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    21.57ms    2.35ms  96.63ms   95.45%
    Req/Sec   232.84     24.62   303.00     72.40%
  556727 requests in 2.00m, 139.11MB read
Requests/sec:   4636.52
Transfer/sec:      1.16MB
```
