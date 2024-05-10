**Pytania teoretyczne**:

- Jakie rozszerzenie powinny mieć programy/skrypty python?
- Co jest niezbędne żeby programować _(uruchamiać skrypt)_ **python**?
- Jak uruchomić progrm/skrpyt python `test` _(gdzie `test` to nazwa pliku z kodem python)_?

**Z1** Wskaz typy zmiennych ustalonych w poniższym kodzie:

```py
a = "squanch"
b = 21.27
c = None
d = "d" 
e = False
f = [1, 2, 3]
g = True
h = 420
```

**Z2** Zbuduj wiadomość `message`, aby po uruchomieniu skryptu zwróciła _"Za 3kg jabłek zapłacisz 16.5zł"_, wykorzystując zmienne `unit`, `count` oraz `unit_price`.

```py
unit = "kg"
count = 3
unit_price = 5.5
message = # ...
print(message)
```

**Z3-Z9** Co zostanie wydrukowane w konsoli po uruchomieniu poniższych skryptów?

**Z3**

```py
a = "6"
b = 9
c = a + str(b) + a
print(c)
d = b + int(a) + b
print(d)
```

**Z4**

```py
array1 = [987, 654, 321]
array2 = ["alfa", "beta", "gamma"]
array1[0] = array2[2]
print(array1)
print(array2)
array2[1] = array1[0]
print(array1)
print(array2)
```

**Z5**

```py
txt = "abcdEFGH...xyz"
print(txt[3])
txt = txt.upper()
print(txt[3])
txt = txt.lower()
print(txt)
```

**Z6**

```py
array = [987, 654, 321]
txt = "abcdEFGH...xyz"
print(len(array))
print(len(txt))
```

**Z7a**

```py
a = True
b = False

if not b and a:
  print("Happy :)")
else:
  print("Sad :(")
```

**Z7b**

```py
a = 20 - 16 / 2
b = 4
b *= b - 1

if a > b:
  print("a > b")
elif a < b:
  print("a < b")
else:
  print("a == b")
```

**Z8a**

```py
value = 4
while value:
  print(value)
  value -= 2
```  

**Z8b**

```py
value = 2
while value < 100:
  value += value - 1
  print(value)
  if value % 11 == 0:
    break
```

**Z9**

```py
array = [3, "2", 7, "5"]
for value in array:
  print(value + value)
```

**Zadanie dodatkowe**: Napisz program, który sumuje dodatnie liczby z wcześniej zadeklarowanej listy. W poniższym kodzie znajduje się przykładowa lista `array`, dla której funkcja `print` wypisze **16**.

```py
array = [4, 1, -2, 8, 3, -5]
# TODO
print(array_sum) # 16
```