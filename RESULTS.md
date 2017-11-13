# Host Info
```
13 Nov 2017

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
Running 1s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   423.10us    1.15ms  20.05ms   96.81%
    Req/Sec    42.48k     2.77k   46.25k    70.00%
  42277 requests in 1.00s, 7.10MB read
Requests/sec:  42269.05
Transfer/sec:      7.09MB
```

## go/go

```
go version go1.9 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 1s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   408.88us  606.53us  12.78ms   95.14%
    Req/Sec    33.01k     2.18k   35.53k    72.73%
  36085 requests in 1.10s, 5.44MB read
Requests/sec:  32804.58
Transfer/sec:      4.94MB
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
Running 1s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.76ms    1.08ms  12.28ms   88.37%
    Req/Sec     2.95k   474.67     3.52k    60.00%
  2938 requests in 1.00s, 751.71KB read
Requests/sec:   2928.03
Transfer/sec:    749.16KB
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
Running 1s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    48.22ms    7.85ms  59.84ms   92.89%
    Req/Sec   226.20     18.20   252.00     70.00%
  225 requests in 1.00s, 138.77KB read
Requests/sec:    224.68
Transfer/sec:    138.57KB
```

## php/slim

```
PHP 7.1.11 (cli) (built: Nov  4 2017 10:39:58) ( NTS )
Copyright (c) 1997-2017 The PHP Group
Zend Engine v3.1.0, Copyright (c) 1998-2017 Zend Technologies
    with Zend OPcache v7.1.11, Copyright (c) 1999-2017, by Zend Technologies
```

```
HappyTest-PASS, ErrorTest-PASS
Running 1s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.07ms    0.86ms  12.60ms   86.97%
    Req/Sec     1.56k    67.01     1.64k    60.00%
  1550 requests in 1.00s, 387.45KB read
Requests/sec:   1549.59
Transfer/sec:    387.34KB
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
Running 1s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.02ms  300.08us   9.45ms   97.51%
    Req/Sec     2.74k   120.69     2.85k    80.00%
  2729 requests in 1.00s, 514.35KB read
Requests/sec:   2725.33
Transfer/sec:    513.66KB
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
Running 1s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.33ms  434.20us  13.48ms   98.65%
    Req/Sec     1.49k    56.12     1.55k    81.82%
  1632 requests in 1.10s, 313.99KB read
Requests/sec:   1484.23
Transfer/sec:    285.55KB
```

## ruby/sinatra

```
ruby 2.4.2p198 (2017-09-14 revision 59899) [x86_64-linux-musl]
sinatra (2.0.0)
sinatra-contrib (2.0.0)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 1s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    44.21ms    7.32ms  56.00ms   88.11%
    Req/Sec   244.60     14.30   262.00     60.00%
  244 requests in 1.00s, 64.75KB read
Requests/sec:    243.50
Transfer/sec:     64.62KB
```
