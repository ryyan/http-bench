# Host Info
```
14 Nov 2017

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
    Latency   392.47us    1.08ms  32.81ms   96.74%
    Req/Sec    45.19k     1.96k   49.14k    70.91%
  494638 requests in 11.00s, 83.02MB read
Requests/sec:  44966.51
Transfer/sec:      7.55MB
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
    Latency   444.32us  759.41us  20.30ms   95.13%
    Req/Sec    33.08k     1.40k   36.71k    68.18%
  361956 requests in 11.00s, 54.54MB read
Requests/sec:  32904.72
Transfer/sec:      4.96MB
```

## java/jersey

```
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.41ms    7.77ms  76.66ms   86.75%
    Req/Sec     4.34k     3.00k   11.03k    67.27%
  47500 requests in 11.00s, 5.53MB read
Requests/sec:   4317.78
Transfer/sec:    514.72KB
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
    Latency     2.55ms  777.71us  12.43ms   92.83%
    Req/Sec     4.39k   618.07     5.17k    84.55%
  48001 requests in 11.00s, 11.99MB read
Requests/sec:   4363.35
Transfer/sec:      1.09MB
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
    Latency    46.09ms    3.61ms  68.07ms   88.11%
    Req/Sec   239.15     15.96   280.00     71.82%
  2623 requests in 11.01s, 1.52MB read
Requests/sec:    238.23
Transfer/sec:    141.15KB
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
    Latency     6.91ms  840.17us  15.55ms   78.88%
    Req/Sec     1.60k    47.01     1.67k    71.82%
  17485 requests in 11.00s, 4.27MB read
Requests/sec:   1589.16
Transfer/sec:    397.22KB
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
yarl          0.14.2 
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.10ms  144.58us   9.81ms   76.98%
    Req/Sec     2.69k    71.61     2.85k    67.27%
  29470 requests in 11.00s, 5.42MB read
Requests/sec:   2678.81
Transfer/sec:    504.89KB
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
    Latency     7.47ms    1.81ms  24.61ms   93.67%
    Req/Sec     1.37k   357.95     1.59k    84.55%
  15033 requests in 11.05s, 2.82MB read
Requests/sec:   1360.99
Transfer/sec:    261.83KB
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
    Latency    45.43ms    3.36ms  59.85ms   93.34%
    Req/Sec   242.60     11.12   260.00     80.91%
  2659 requests in 11.00s, 684.59KB read
Requests/sec:    241.63
Transfer/sec:     62.21KB
```
