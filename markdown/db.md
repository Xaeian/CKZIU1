![Redis](redis.webp)

https://github.com/tporadowski/redis/releases

```bash
tasklist | findstr /R "redis-server.exe"
```

Redis

`Win`+`R` --> `services.msc` --> Redis
`sysdm.cpl` 
`C:\Program Files\Redis`


Dane przechwoywane w pamięci RAM

<!-- Idealne do przerzutu danych pomiędzy -->


```
SET mystr "myvalue"
GET mystr
MSET key1 "value1" key2 "value2"
MGET key1 key2
```

```
RPUSH mylist "one" "two" "three"
LPOP mylist
LRANGE mylist 0 -1


RPUSHX mylist "value"
HMSET myhash field1 "Hello" field2 "World"
HGET myhash field1
```

```
DEL mykey
```

```
ZREVRANGE myset start stop
SMEMBERS myset
```

```bash
FLUSHDB
```
