# Host Info
```
30 Aug 2021

Linux 4.19.104-microsoft-standard

Client:
 Version:           20.10.7
 API version:       1.41
 Go version:        go1.13.8
 Git commit:        20.10.7-0ubuntu1~20.04.1
 Built:             Wed Aug  4 22:52:25 2021
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.8
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.16.6
  Git commit:       75249d8
  Built:            Fri Jul 30 19:52:10 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.9
  GitCommit:        e25210fe30a0a703442421b0f60afac609f950a3
 runc:
  Version:          1.0.1
  GitCommit:        v1.0.1-0-g4144b63
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

---

# Benchmarks

## go/fasthttp

```
Getting info for httpbench-go-fasthttp
go version go1.17 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.12ms    0.89ms  10.80ms   81.18%
    Req/Sec     4.94k   268.03     8.74k    76.10%
  649545 requests in 33.10s, 109.02MB read
Requests/sec:  19623.82
Transfer/sec:      3.29MB
```

## go/go

```
Getting info for httpbench-go-go
go version go1.17 linux/amd64
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   705.86us  501.82us   9.27ms   82.29%
    Req/Sec     7.44k   263.54     9.47k    71.88%
  978905 requests in 33.10s, 147.50MB read
Requests/sec:  29574.23
Transfer/sec:      4.46MB
```

## java/jersey

```
Getting info for httpbench-java-jersey
openjdk version "16.0.2" 2021-07-20
OpenJDK Runtime Environment (build 16.0.2+7-67)
OpenJDK 64-Bit Server VM (build 16.0.2+7-67, mixed mode, sharing)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.42ms    1.69ms 101.46ms   93.70%
    Req/Sec     4.22k   767.49     5.25k    89.39%
  554643 requests in 33.00s, 64.57MB read
Requests/sec:  16805.10
Transfer/sec:      1.96MB
```

## java/spark

```
Getting info for httpbench-java-spark
openjdk version "16.0.2" 2021-07-20
OpenJDK Runtime Environment (build 16.0.2+7-67)
OpenJDK 64-Bit Server VM (build 16.0.2+7-67, mixed mode, sharing)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.44ms    1.53ms  62.12ms   89.42%
    Req/Sec     4.01k   610.49    13.80k    94.32%
  527175 requests in 33.10s, 105.58MB read
Requests/sec:  15926.78
Transfer/sec:      3.19MB
```

## node/express

```
Getting info for httpbench-node-express
v16.8.0
[0mexpress@ /app[0m
[0m+-- [33m[40mexpress@4.17.1[49m[39m[0m
[0m`-- [33m[40muuid@8.3.2[49m[39m[0m
[0m[0m
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.09ms    1.25ms  23.29ms   90.21%
    Req/Sec     0.99k    97.29     1.16k    74.62%
  129814 requests in 33.02s, 35.28MB read
Requests/sec:   3931.85
Transfer/sec:      1.07MB
```

## node/server

```
Getting info for httpbench-node-server
v16.8.0
[0mserver@ /app[0m
[0m+-- server@1.0.35[0m
[0m| `-- [33m[40mexpress@4.17.1[49m[39m[0m
[0m`-- [33m[40muuid@8.3.2[49m[39m[0m
[0m[0m
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    50.80ms    2.92ms  71.34ms   91.59%
    Req/Sec    98.77      5.44   121.00     86.67%
  12991 requests in 33.03s, 7.79MB read
Requests/sec:    393.34
Transfer/sec:    241.45KB
```

## php/slim

```
Getting info for httpbench-php-slim
PHP 8.0.10 (cli) (built: Aug 26 2021 21:59:02) ( NTS )
Copyright (c) The PHP Group
Zend Engine v4.0.10, Copyright (c) Zend Technologies
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   209.99ms    9.13ms 225.91ms   99.30%
    Req/Sec    23.79     11.03    40.00     50.96%
  3134 requests in 33.04s, 627.41KB read
  Socket errors: connect 0, read 3134, write 0, timeout 0
Requests/sec:     94.84
Transfer/sec:     18.99KB
```

## python/aiohttp

```
Getting info for httpbench-python-aiohttp
Python 3.9.6
Package           Version
----------------- -----------
aiohttp           3.7.4.post0
async-timeout     3.0.1
attrs             21.2.0
cchardet          2.1.7
chardet           4.0.0
idna              3.2
multidict         5.1.0
pip               21.2.4
setuptools        57.4.0
typing-extensions 3.10.0.1
wheel             0.37.0
yarl              1.6.3
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.98ms  191.83us  11.57ms   66.17%
    Req/Sec   839.70     22.10     0.90k    73.71%
  110345 requests in 33.02s, 20.94MB read
Requests/sec:   3342.00
Transfer/sec:    649.47KB
```

## python/flask

```
Getting info for httpbench-python-flask
Python 3.9.6
Package      Version
------------ -------
click        8.0.1
Flask        2.0.1
itsdangerous 2.0.1
Jinja2       3.0.1
MarkupSafe   2.0.1
pip          21.2.4
setuptools   57.4.0
Werkzeug     2.0.1
wheel        0.37.0
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    24.26ms    2.07ms  35.88ms   68.42%
    Req/Sec   206.16     16.83   252.00     76.44%
  27114 requests in 33.02s, 5.07MB read
Requests/sec:    821.02
Transfer/sec:    157.15KB
```

## ruby/sinatra

```
Getting info for httpbench-ruby-sinatra
ruby 3.0.2p107 (2021-07-07 revision 0db68f0233) [x86_64-linux]

*** LOCAL GEMS ***

sinatra (2.1.0)
sinatra-contrib (2.1.0)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.18ms    1.03ms  12.12ms   66.17%
    Req/Sec     0.92k   466.56     1.53k    53.79%
  60387 requests in 33.05s, 8.87MB read
Requests/sec:   1827.42
Transfer/sec:    274.83KB
```

## rust/gotham

```
Getting info for httpbench-rust-gotham
rustc 1.54.0 (a178d0322 2021-07-26)
```

```
HappyTest-PASS, ErrorTest-PASS
Running 33s test @ http://127.0.0.1:8888/echo/HelloWorld?num=1234567890
  4 threads and 20 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   353.75us  140.67us   5.43ms   76.28%
    Req/Sec    13.67k   784.59    15.25k    68.50%
  1800417 requests in 33.10s, 358.86MB read
Requests/sec:  54394.16
Transfer/sec:     10.84MB
```
