# Host Info
```
11 Nov 2017

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

## go/fasthttp

```
go version go1.9 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   400.92us    1.10ms  28.32ms   96.54%
    Req/Sec    45.69k     1.78k   49.32k    73.87%
  504485 requests in 11.10s, 84.68MB read
Requests/sec:  45446.88
Transfer/sec:      7.63MB
```

## go/go

```
go version go1.9 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   449.22us  802.09us  22.55ms   95.36%
    Req/Sec    33.17k     1.19k   36.55k    73.64%
  362933 requests in 11.00s, 54.69MB read
Requests/sec:  32992.60
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
    Latency     2.52ms  750.93us  12.81ms   93.33%
    Req/Sec     4.45k   561.38     5.04k    85.45%
  48682 requests in 11.00s, 12.16MB read
Requests/sec:   4425.54
Transfer/sec:      1.11MB
```

## python/aiohttp

```
Python 3.6.3
Package       Version
------------- -------
aiohttp       2.3.2  
async-timeout 2.0.0  
cchardet      2.1.1  
chardet       3.0.4  
multidict     3.3.2  
pip           9.0.1  
setuptools    36.6.0 
wheel         0.30.0 
yarl          0.14.0 
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.15ms  150.98us  10.48ms   85.25%
    Req/Sec     2.66k    69.44     2.80k    70.00%
  29133 requests in 11.00s, 5.36MB read
Requests/sec:   2648.26
Transfer/sec:    499.13KB
```
