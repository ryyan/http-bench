# Host Info
```
17 Nov 2017

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
    Latency   386.44us    1.00ms  26.40ms   96.49%
    Req/Sec    45.22k     1.51k   49.37k    77.27%
  494743 requests in 11.00s, 83.04MB read
Requests/sec:  44975.43
Transfer/sec:      7.55MB
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
    Latency   451.87us  816.39us  22.36ms   95.17%
    Req/Sec    33.64k     1.52k   36.10k    72.73%
  368154 requests in 11.00s, 55.47MB read
Requests/sec:  33466.66
Transfer/sec:      5.04MB
```

## java/jersey

```
openjdk version "1.8.0_151"
OpenJDK Runtime Environment (build 1.8.0_151-8u151-b12-1~deb9u1-b12)
OpenJDK 64-Bit Server VM (build 25.151-b12, mixed mode)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.18ms    7.59ms  78.44ms   87.14%
    Req/Sec     4.59k     3.00k   11.67k    64.55%
  50217 requests in 11.00s, 5.85MB read
Requests/sec:   4564.93
Transfer/sec:    544.19KB
```

## java/spark

```
openjdk version "1.8.0_151"
OpenJDK Runtime Environment (build 1.8.0_151-8u151-b12-1~deb9u1-b12)
OpenJDK 64-Bit Server VM (build 25.151-b12, mixed mode)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.88ms    3.13ms  44.27ms   92.15%
    Req/Sec     9.80k     3.24k   13.38k    75.68%
  108194 requests in 11.10s, 21.57MB read
Requests/sec:   9747.05
Transfer/sec:      1.94MB
```

## node/express

```
v9.2.0
express@ /app
+-- [40m[33mexpress@4.16.2[39m[49m 
`-- [40m[33muuid@3.1.0[39m[49m 

```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.40ms  722.13us  12.59ms   92.54%
    Req/Sec     4.67k   622.05     5.38k    84.55%
  51102 requests in 11.00s, 12.77MB read
Requests/sec:   4645.23
Transfer/sec:      1.16MB
```

## node/server

```
v9.2.0
server@ /app
+-- server@1.0.5
| `-- [40m[33mexpress@4.16.2[39m[49m 
`-- [40m[33muuid@3.1.0[39m[49m 

```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    45.58ms    3.40ms  68.08ms   91.39%
    Req/Sec   241.49     14.94   272.00     68.18%
  2647 requests in 11.01s, 1.53MB read
Requests/sec:    240.50
Transfer/sec:    142.59KB
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
    Latency     5.80ms  796.61us  16.04ms   77.85%
    Req/Sec     1.90k    55.18     1.98k    67.27%
  20840 requests in 11.00s, 5.09MB read
Requests/sec:   1894.46
Transfer/sec:    473.53KB
```

## python/aiohttp

```
Python 3.6.3
Package       Version
------------- -------
aiohttp       2.3.3  
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
    Latency     4.10ms  184.57us   9.18ms   79.97%
    Req/Sec     2.69k    87.06     2.84k    70.00%
  29475 requests in 11.00s, 5.43MB read
Requests/sec:   2679.22
Transfer/sec:    504.97KB
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
    Latency     7.53ms    1.71ms  30.34ms   94.49%
    Req/Sec     1.37k   330.04     1.57k    85.45%
  15002 requests in 11.03s, 2.82MB read
Requests/sec:   1359.93
Transfer/sec:    261.63KB
```

## ruby/sinatra

```
ruby 2.4.2p198 (2017-09-14 revision 59899) [x86_64-linux-musl]

*** LOCAL GEMS ***

sinatra (2.0.0)
sinatra-contrib (2.0.0)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    45.43ms    3.35ms  64.86ms   93.00%
    Req/Sec   242.55     10.32   260.00     76.36%
  2658 requests in 11.02s, 684.75KB read
Requests/sec:    241.12
Transfer/sec:     62.12KB
```

## rust/nickel

```
rustc 1.21.0 (3b72af97e 2017-10-09)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   149.67us   74.44us   2.90ms   78.15%
    Req/Sec    31.57k   643.76    34.24k    74.55%
  345447 requests in 11.02s, 63.25MB read
Requests/sec:  31341.59
Transfer/sec:      5.74MB
```
