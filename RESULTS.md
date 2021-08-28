# Host Info
```
07 Apr 2018

Linux 4.9.0-6-amd64

Client:
 Version:	18.03.0-ce
 API version:	1.37
 Go version:	go1.9.4
 Git commit:	0520e24
 Built:	Wed Mar 21 23:10:06 2018
 OS/Arch:	linux/amd64
 Experimental:	false
 Orchestrator:	swarm

Server:
 Engine:
  Version:	18.03.0-ce
  API version:	1.37 (minimum version 1.12)
  Go version:	go1.9.4
  Git commit:	0520e24
  Built:	Wed Mar 21 23:08:35 2018
  OS/Arch:	linux/amd64
  Experimental:	false
```

---

# Benchmarks

## go/fasthttp

```
go version go1.10.1 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   401.90us  785.40us  21.98ms   96.88%
    Req/Sec    33.49k     1.61k   37.08k    77.48%
  369718 requests in 11.10s, 62.06MB read
Requests/sec:  33308.67
Transfer/sec:      5.59MB
```

## go/go

```
go version go1.10.1 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   535.40us    0.89ms  22.50ms   95.63%
    Req/Sec    25.65k     1.37k   28.05k    93.64%
  280673 requests in 11.00s, 42.29MB read
Requests/sec:  25513.16
Transfer/sec:      3.84MB
```

## java/jersey

```
openjdk version "1.8.0_162"
OpenJDK Runtime Environment (build 1.8.0_162-8u162-b12-1~deb9u1-b12)
OpenJDK 64-Bit Server VM (build 25.162-b12, mixed mode)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.40ms    5.72ms  68.39ms   87.32%
    Req/Sec     4.07k     2.53k   11.08k    70.91%
  44588 requests in 11.00s, 5.19MB read
Requests/sec:   4052.94
Transfer/sec:    483.15KB
```

## java/spark

```
openjdk version "1.8.0_162"
OpenJDK Runtime Environment (build 1.8.0_162-8u162-b12-1~deb9u1-b12)
OpenJDK 64-Bit Server VM (build 25.162-b12, mixed mode)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.73ms    2.51ms  49.56ms   92.06%
    Req/Sec     9.02k     3.28k   12.05k    73.64%
  98755 requests in 11.00s, 19.68MB read
Requests/sec:   8977.15
Transfer/sec:      1.79MB
```

## node/express

```
v9.11.1
express@ /app
+-- [40m[33mexpress@4.16.3[39m[49m 
`-- [40m[33muuid@3.2.1[39m[49m 

```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.47ms  737.59us  12.78ms   92.94%
    Req/Sec     4.51k   578.25     5.01k    89.09%
  49362 requests in 11.00s, 12.33MB read
Requests/sec:   4487.32
Transfer/sec:      1.12MB
```

## node/server

```
v9.11.1
server@ /app
+-- server@1.0.18
| `-- [40m[33mexpress@4.16.3[39m[49m 
`-- [40m[33muuid@3.2.1[39m[49m 

```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    44.57ms    2.77ms  68.16ms   86.94%
    Req/Sec   247.24     17.30   300.00     77.27%
  2710 requests in 11.01s, 1.57MB read
Requests/sec:    246.23
Transfer/sec:    146.01KB
```

## php/slim

```
PHP 7.1.12 (cli) (built: Dec  1 2017 19:26:10) ( NTS )
Copyright (c) 1997-2017 The PHP Group
Zend Engine v3.1.0, Copyright (c) 1998-2017 Zend Technologies
    with Zend OPcache v7.1.12, Copyright (c) 1999-2017, by Zend Technologies
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.00ms    0.87ms  16.41ms   77.65%
    Req/Sec     1.84k    75.74     1.94k    83.64%
  20124 requests in 11.00s, 4.91MB read
Requests/sec:   1828.91
Transfer/sec:    457.14KB
```

## python/aiohttp

```
Python 3.6.5
Package       Version
------------- -------
aiohttp       3.1.2  
async-timeout 2.0.1  
attrs         17.4.0 
cchardet      2.1.1  
chardet       3.0.4  
idna          2.6    
idna-ssl      1.0.1  
multidict     4.1.0  
pip           9.0.3  
setuptools    39.0.1 
wheel         0.30.0 
yarl          1.1.1  
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.49ms  255.34us  13.64ms   90.03%
    Req/Sec     2.46k   106.20     2.63k    78.18%
  26904 requests in 11.00s, 4.95MB read
Requests/sec:   2445.74
Transfer/sec:    460.98KB
```

## python/flask

```
Python 3.6.5
Package      Version
------------ -------
click        6.7    
Flask        0.12.2 
itsdangerous 0.24   
Jinja2       2.10   
MarkupSafe   1.0    
pip          9.0.3  
setuptools   39.0.1 
Werkzeug     0.14.1 
wheel        0.30.0 
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.70ms    1.86ms  27.32ms   95.18%
    Req/Sec     1.35k   328.40     1.51k    88.18%
  14806 requests in 11.04s, 2.78MB read
Requests/sec:   1341.46
Transfer/sec:    258.07KB
```

## ruby/sinatra

```
ruby 2.5.1p57 (2018-03-29 revision 63029) [x86_64-linux-musl]

*** LOCAL GEMS ***

sinatra (2.0.1)
sinatra-contrib (2.0.1)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    43.98ms    2.16ms  60.86ms   97.20%
    Req/Sec   250.50     20.82   300.00     70.00%
  2749 requests in 11.05s, 708.33KB read
Requests/sec:    248.84
Transfer/sec:     64.12KB
```

## rust/nickel

```
rustc 1.25.0 (84203cac6 2018-03-25)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   181.16us   98.12us   5.74ms   80.18%
    Req/Sec    24.50k   407.03    25.76k    73.64%
  268128 requests in 11.00s, 49.10MB read
Requests/sec:  24374.02
Transfer/sec:      4.46MB
```
