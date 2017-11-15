# Host Info
```
15 Nov 2017

Linux 4.13.0-16-generic

Client:
 Version:      17.09.0-ce
 API version:  1.32
 Go version:   go1.8.3
 Git commit:   afdb6d4
 Built:        Tue Sep 26 22:42:45 2017
 OS/Arch:      linux/amd64

Server:
 Version:      17.09.0-ce
 API version:  1.32 (minimum version 1.12)
 Go version:   go1.8.3
 Git commit:   afdb6d4
 Built:        Tue Sep 26 22:41:24 2017
 OS/Arch:      linux/amd64
 Experimental: false
```

---

# Benchmarks

## go/fasthttp

```
go version go1.9.2 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   391.04us    1.00ms  20.84ms   96.51%
    Req/Sec    44.57k     2.27k   48.67k    73.87%
  492027 requests in 11.10s, 82.59MB read
Requests/sec:  44326.77
Transfer/sec:      7.44MB
```

## go/go

```
go version go1.9.2 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   455.58us    0.86ms  23.28ms   95.57%
    Req/Sec    33.16k     1.20k   36.17k    68.18%
  363021 requests in 11.00s, 54.70MB read
  Socket errors: connect 0, read 1, write 0, timeout 0
Requests/sec:  32999.05
Transfer/sec:      4.97MB
```

## java/jersey

```
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.13ms    7.41ms  71.55ms   86.81%
    Req/Sec     4.63k     3.16k   11.52k    64.55%
  50686 requests in 11.00s, 5.90MB read
Requests/sec:   4607.12
Transfer/sec:    549.22KB
```

## node/express

```
v9.1.0
express@ /app
+-- express@4.16.2 
`-- uuid@3.1.0 

```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.39ms  713.56us  12.40ms   92.45%
    Req/Sec     4.68k   618.08     5.57k    84.55%
  51233 requests in 11.00s, 12.80MB read
Requests/sec:   4657.04
Transfer/sec:      1.16MB
```

## node/server

```
v9.1.0
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
    Latency    45.91ms    3.47ms  60.17ms   89.25%
    Req/Sec   240.38     14.90   282.00     67.27%
  2632 requests in 11.00s, 1.52MB read
Requests/sec:    239.18
Transfer/sec:    141.70KB
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
    Latency     5.73ms  731.84us  13.66ms   75.82%
    Req/Sec     1.93k    52.81     2.01k    70.00%
  21079 requests in 11.00s, 5.15MB read
Requests/sec:   1915.84
Transfer/sec:    478.87KB
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
    Latency     4.12ms  204.19us  10.83ms   86.40%
    Req/Sec     2.68k    75.93     2.86k    72.73%
  29321 requests in 11.00s, 5.40MB read
Requests/sec:   2665.47
Transfer/sec:    502.38KB
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
    Latency     7.28ms    1.14ms  23.41ms   92.77%
    Req/Sec     1.43k   232.16     1.57k    92.73%
  15656 requests in 11.01s, 2.94MB read
Requests/sec:   1421.69
Transfer/sec:    273.51KB
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
    Latency    45.17ms    3.11ms  65.23ms   94.17%
    Req/Sec   243.85     10.32   262.00     75.45%
  2674 requests in 11.02s, 688.86KB read
Requests/sec:    242.56
Transfer/sec:     62.49KB
```
