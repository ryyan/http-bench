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
    Latency   437.72us  769.70us  17.78ms   95.53%
    Req/Sec    33.07k     1.60k   36.86k    71.82%
  361806 requests in 11.00s, 54.52MB read
Requests/sec:  32890.00
Transfer/sec:      4.96MB
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
    Latency     2.50ms  746.95us  12.54ms   92.98%
    Req/Sec     4.48k   562.96     4.98k    89.09%
  48990 requests in 11.00s, 12.24MB read
Requests/sec:   4453.47
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
yarl          0.13.0 
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.10ms  181.24us  11.51ms   83.37%
    Req/Sec     2.70k    85.30     2.84k    60.91%
  29522 requests in 11.00s, 5.43MB read
Requests/sec:   2683.63
Transfer/sec:    505.80KB
```
