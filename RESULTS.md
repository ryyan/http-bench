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
    Latency   385.53us    1.01ms  26.92ms   96.53%
    Req/Sec    45.23k     1.48k   48.12k    73.64%
  494833 requests in 11.00s, 83.06MB read
Requests/sec:  44983.53
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
    Latency   455.33us  815.80us  23.04ms   95.15%
    Req/Sec    33.41k     1.58k   36.40k    77.27%
  365814 requests in 11.00s, 55.12MB read
Requests/sec:  33254.46
Transfer/sec:      5.01MB
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
    Latency     4.92ms    7.40ms  69.18ms   87.19%
    Req/Sec     5.22k     3.55k   11.23k    56.36%
  57153 requests in 11.00s, 6.65MB read
Requests/sec:   5195.48
Transfer/sec:    619.36KB
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
    Latency     1.86ms    3.17ms  47.01ms   92.35%
    Req/Sec    10.04k     3.28k   14.16k    72.73%
  109837 requests in 11.00s, 21.89MB read
Requests/sec:   9982.18
Transfer/sec:      1.99MB
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
    Latency     2.41ms  727.05us  14.34ms   92.78%
    Req/Sec     4.65k   602.29     5.31k    88.18%
  50841 requests in 11.00s, 12.70MB read
Requests/sec:   4621.43
Transfer/sec:      1.15MB
```

## node/server

```
v9.2.0
server@ /app
+-- server@1.0.4
| `-- [40m[33mexpress@4.16.2[39m[49m 
`-- [40m[33muuid@3.1.0[39m[49m 

```

```
HappyTest-PASS, ErrorTest-PASS
Running 11s test @ http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  1 threads and 11 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    45.64ms    3.41ms  68.05ms   90.96%
    Req/Sec   241.24     15.75   282.00     72.73%
  2644 requests in 11.00s, 1.53MB read
Requests/sec:    240.26
Transfer/sec:    142.46KB
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
    Latency     5.76ms  790.82us  15.00ms   76.29%
    Req/Sec     1.92k    42.15     2.00k    64.55%
  20965 requests in 11.00s, 5.12MB read
Requests/sec:   1905.33
Transfer/sec:    476.24KB
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
    Latency     4.08ms  175.64us  11.84ms   79.68%
    Req/Sec     2.71k    82.37     2.88k    68.47%
  29885 requests in 11.10s, 5.50MB read
Requests/sec:   2692.32
Transfer/sec:    507.44KB
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
    Latency     7.54ms    1.70ms  27.29ms   94.22%
    Req/Sec     1.37k   329.78     1.55k    86.36%
  15000 requests in 11.07s, 2.82MB read
Requests/sec:   1355.51
Transfer/sec:    260.78KB
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
    Latency    45.28ms    3.25ms  59.97ms   94.04%
    Req/Sec   243.35      9.69   262.00     79.09%
  2666 requests in 11.02s, 686.39KB read
Requests/sec:    241.86
Transfer/sec:     62.27KB
```
