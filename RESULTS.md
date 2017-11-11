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
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.95ms    1.62ms  36.93ms   93.29%
    Req/Sec     7.94k   819.98    30.76k    74.19%
  3794436 requests in 2.00m, 571.75MB read
Requests/sec:  31594.12
Transfer/sec:      4.76MB
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
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.26ms  818.27us  18.91ms   95.52%
    Req/Sec     1.19k    67.59     1.90k    83.94%
  567357 requests in 2.00m, 141.76MB read
Requests/sec:   4725.49
Transfer/sec:      1.18MB
```
