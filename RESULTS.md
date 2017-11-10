10 Nov 2017, 11:35

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

##go/go

```
go version go1.9 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 10s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   643.43us    1.58ms  26.69ms   94.27%
    Req/Sec    16.24k     1.37k   29.22k    83.08%
  324938 requests in 10.10s, 48.96MB read
Requests/sec:  32171.97
Transfer/sec:      4.85MB
```
