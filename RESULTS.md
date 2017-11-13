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
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   418.03us    1.22ms  32.47ms   96.56%
    Req/Sec    45.52k     2.09k   49.46k    75.68%
  502484 requests in 11.10s, 84.34MB read
Requests/sec:  45268.92
Transfer/sec:      7.60MB
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
    Latency   436.08us  715.32us  17.77ms   95.17%
    Req/Sec    32.66k     1.33k   35.19k    70.27%
  360731 requests in 11.10s, 54.36MB read
Requests/sec:  32497.51
Transfer/sec:      4.90MB
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
    Latency     2.51ms  755.76us  12.45ms   92.94%
    Req/Sec     4.45k   573.64     5.02k    89.09%
  48744 requests in 11.00s, 12.18MB read
Requests/sec:   4430.65
Transfer/sec:      1.11MB
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
    Latency    46.17ms    3.74ms  68.31ms   87.97%
    Req/Sec   238.88     19.64   290.00     80.91%
  2619 requests in 11.01s, 1.51MB read
Requests/sec:    237.91
Transfer/sec:    140.75KB
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
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.90ms  823.54us  14.98ms   77.15%
    Req/Sec     1.60k    47.34     1.67k    69.09%
  17520 requests in 11.00s, 4.28MB read
Requests/sec:   1592.34
Transfer/sec:    398.01KB
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
    Latency     4.11ms  177.66us  11.48ms   81.91%
    Req/Sec     2.69k    82.54     2.84k    66.36%
  29452 requests in 11.00s, 5.42MB read
Requests/sec:   2677.32
Transfer/sec:    504.61KB
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
    Latency     7.42ms    1.86ms  25.37ms   93.69%
    Req/Sec     1.37k   379.08     1.61k    83.64%
  14978 requests in 11.04s, 2.81MB read
Requests/sec:   1356.69
Transfer/sec:    261.00KB
```

## ruby/sinatra

```
ruby 2.4.2p198 (2017-09-14 revision 59899) [x86_64-linux-musl]
sinatra (2.0.0)
sinatra-contrib (2.0.0)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    45.25ms    3.10ms  58.13ms   94.08%
    Req/Sec   243.61     11.64   270.00     74.55%
  2669 requests in 11.00s, 687.58KB read
Requests/sec:    242.57
Transfer/sec:     62.49KB
```
