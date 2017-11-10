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

## go/go

```
go version go1.9 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 30s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.93ms    1.54ms  32.41ms   93.13%
    Req/Sec     8.01k   767.52    10.75k    70.33%
  957328 requests in 30.04s, 144.25MB read
Requests/sec:  31872.45
Transfer/sec:      4.80MB
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
Running 30s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.42ms    0.89ms  17.50ms   93.82%
    Req/Sec     1.14k    98.59     1.29k    91.92%
  136611 requests in 30.02s, 34.13MB read
Requests/sec:   4550.99
Transfer/sec:      1.14MB
```
