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
    Latency   401.06us    1.07ms  24.16ms   96.36%
    Req/Sec    45.68k     1.95k   48.39k    69.09%
  499716 requests in 11.00s, 83.88MB read
Requests/sec:  45427.39
Transfer/sec:      7.62MB
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
    Latency   437.05us  734.16us  16.77ms   95.26%
    Req/Sec    33.03k     1.60k   36.56k    66.36%
  361488 requests in 11.00s, 54.47MB read
Requests/sec:  32860.03
Transfer/sec:      4.95MB
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
    Latency     2.52ms  746.87us  12.66ms   93.06%
    Req/Sec     4.44k   561.11     5.06k    88.18%
  48527 requests in 11.00s, 12.13MB read
Requests/sec:   4410.71
Transfer/sec:      1.10MB
```

## node/server

```
v8.6.0
server@ /app
+-- server@1.0.4
| `-- express@4.16.2 
`-- uuid@3.1.0 

```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    46.85ms    3.83ms  64.23ms   83.32%
    Req/Sec   235.33     17.44   290.00     86.36%
  2578 requests in 11.01s, 1.49MB read
Requests/sec:    234.24
Transfer/sec:    138.82KB
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
    Latency     4.09ms  185.70us  11.94ms   84.20%
    Req/Sec     2.70k    81.03     2.86k    67.57%
  29866 requests in 11.10s, 5.50MB read
Requests/sec:   2690.54
Transfer/sec:    507.10KB
```

## python/flask

```
Python 3.6.3
Package      Version
------------ -------
click        6.7    
Flask        0.12.2 
itsdangerous 0.24   
Jinja2       2.10   
MarkupSafe   1.0    
pip          9.0.1  
setuptools   36.6.0 
Werkzeug     0.12.2 
wheel        0.30.0 
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.62ms    1.78ms  26.87ms   94.50%
    Req/Sec     1.36k   335.43     1.54k    86.36%
  14934 requests in 11.05s, 2.81MB read
Requests/sec:   1351.02
Transfer/sec:    259.91KB
```
