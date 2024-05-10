import redis

# Tworzenie połączenia z lokalnym serwerem Redis

# r = redis.Redis(host='localhost', port=6379, db=0)
r = redis.Redis(
  username="default",
  password="x03DNV0kn7sHkDxV8iLsswIpZ8ubNcnP",
  host='redis-18749.c1.us-central1-2.gce.redns.redis-cloud.com',
  port=18749,
  db=0
)

# r.set("test-web", "test-value")
value = r.get('test-web')
print(value)




# ```
# RPUSH mylist "one" "two" "three"
# LPOP mylist
# LRANGE mylist 0 -1

# lista = r.lrange('lista', 0, -1)
# print(lista)






# Ustawienie wartości
# r.set('klucz', 'wartosc')

# Pobranie wartości

# Dodanie elementu do listy
# r.rpush('lista', 'element1')
# r.rpush('lista', 'element2')

# Pobranie elementów listy


# default
# x03DNV0kn7sHkDxV8iLsswIpZ8ubNcnP


