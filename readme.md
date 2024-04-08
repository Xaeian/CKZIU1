**Pytania teoretyczne**:

- Jakie rozszerzenie powinny mieć programy/skrypty python?
- Co jest niezbędne żeby programować _(uruchamiać skrpt)_ **python**?
- Jak uruchomić progrm/skrpyt python `test` _(gdzie `test` to nazwa pliku z kodem python)_?

**Z1** Wskaz typy zmiennych ustalonych w poniższym kodzie _(odpowiedzi w komentarzach)_:

```py
a = 7 # int
b = 2.3 # float
c = "text" # str
d = True # bool
e = None # NoneType
f = [7, 2.3, "text"] # list
```

**Z2** Zbuduj wiadomość `hello`, aby po uruchomieniu skryptu zwróciła _"Jestem Ola mam 10 lat"_, wykorzystując zmienne `name` oraz `year`.

```py
name = "Ola"
year = 10
hello = # ...
print(hello) # 
```

**Pozostałe zadania** - Co zostanie wydrukowane w konsoli po uruchomieniu poniższych skryptów?:

**Z3a**

```py
a = 5
b = "10"
msg = a + b
print(msg)
```

**Z3b**

```py
a = 5
b = "10"
msg = str(a) + b
print(msg)
```

**Z3c**

```py
a = 5
b = "10"
msg = a + int(b)
print(msg)
```

**Z4a**

```py
array = [1, 2, 3]
array[1] = 4
print(array)
```

**Z4b**

```py
array1 = [1, 2, 3]
array2 = ["a", "b", "c"]
array1[0] = array2[2]
print(array1)
print(array2)
array2[1] = array1[0]
print(array1)
print(array2)
```

**Z5a**

```py
txt = "Xenomorf"
txt = txt.upper()
print(txt)
```

**Z5b**

```py
txt = "Xenomorf"
print(txt[2])
```

**Z6**

```py
array = [1, 2, 3]
txt = "Xenomorf"
print(len(array))
print(len(txt))
```

**Z7a**

```py
value = True

if not value:
  print("Happy :)")
else:
  print("Sad :(")
```

**Z7b**

```py
year = 16
year += 2
print("Czas na ...")

if year < 25 and year > 19:
    print("... studia")
elif year <= 19:
    print("... szkołę")
else:
    print("... pracę")
```

**Z7c**

```py
x = 7
y = 2 * x + 3
print(y)

if x > 15:
  print("Dużo!")
else:
  print("Mało!")
```

**Z7d**

```py
value = 2
value *= 4
value = value - 3

print("Let's go!")

if not (value < 7 or value > 20):
  print(":*")
else:
  value = value + 10 * 2
  if value > 28:
    print(":)")
  else:
    print(":(")
```

**Z8a**

```py
value = 3
while value:
  print(value)
  value = value - 1
```  

**Z8b**

```py
value = 3
while value < 10:
  value += 2
  print(value)
```

**Z8c**

```py 
value = 3
while value < 10:
  value += 1
  if value == 7: continue
  print(value)
```

**Z8d**

```py
value = 3
while value < 10:
  value += 1
  if value == 7: break
  print(value)
```

**Z9**

```py
array = [3, 2, 4]
for value in array:
  print(value * value)
```
