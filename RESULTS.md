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
    Latency   382.86us    0.99ms  23.64ms   96.54%
    Req/Sec    45.70k     1.91k   49.39k    70.00%
  500136 requests in 11.00s, 83.95MB read
Requests/sec:  45464.19
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
    Latency   443.59us  796.39us  20.42ms   95.40%
    Req/Sec    33.54k     1.29k   36.04k    76.58%
  370340 requests in 11.10s, 55.80MB read
Requests/sec:  33363.50
Transfer/sec:      5.03MB
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
    Latency     2.52ms  743.44us  12.28ms   93.01%
    Req/Sec     4.45k   567.27     5.08k    87.27%
  48654 requests in 11.00s, 12.16MB read
Requests/sec:   4422.76
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
    Latency    46.38ms    3.79ms  68.14ms   86.20%
    Req/Sec   237.35     15.29   290.00     67.27%
  2602 requests in 11.01s, 1.51MB read
Requests/sec:    236.35
Transfer/sec:    140.04KB
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
    Latency     4.02ms  175.10us  12.02ms   87.88%
    Req/Sec     2.75k    73.84     2.88k    68.18%
  30097 requests in 11.00s, 5.54MB read
Requests/sec:   2735.91
Transfer/sec:    515.65KB
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
    Latency     7.45ms    1.80ms  23.54ms   93.95%
    Req/Sec     1.37k   365.57     1.61k    84.55%
  15035 requests in 11.04s, 2.82MB read
Requests/sec:   1362.17
Transfer/sec:    262.06KB
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
    Latency    45.57ms    3.53ms  64.01ms   92.57%
    Req/Sec   241.80     10.28   262.00     77.27%
  2650 requests in 11.03s, 682.49KB read
Requests/sec:    240.35
Transfer/sec:     61.90KB
```
