Markdown jest technologią przeznaczonado tworzenia dokumentów tekstowych, czyli tak jak MS Word, jednak różnic między tymi narzędziami jest więcej niż podobieństw. MS Word jest zoriętowany pod tworzenie 

Kod Markdown jest konwertowany na **HTML**, ale jest znacznie prostszy od niego, co czyni go najłatwiejszym sposobem publikowania treści/dokumentów w internecie.

W dokumencie znajdziesz elementy składni **Markdown**, zarówno te bardziej, jak i mniej przydatne. 

## Nagłówki

Aby utworzyć nagłówek, na początku nowej linii umieść `#`. Liczba użytych znaków `#` odpowiada poziomowi nagłówka.

```md
# Tytuł
## Rozdział
### Podrozdział
#### Sekcja
##### Podsekcja
```

Aby mocno wyodrębnić jakieś fragmenty tekstu bez dodawania nagłówka, możemy wstawić linię poziomą:

```
---
```

---

## Wyróżnianie tekstu

Możemy wyróżnić istotne fragmenty tekstu na kilka sposobów

```md
**Tekst pogrubiony**
_Tekst pochylony_
`Tekst jako code`
~~Tekst przekreślony~~
==Tekst podświetlony==
> Tekst jako cytat
```

**Tekst pogrubiony**

_Tekst pochylony_

`Tekst jako code`

~~Tekst przekreślony~~

==Tekst podświetlony==

> Tekst jako cytat

### Indeksy

```md
Index dolny: H~2~O
Index górny: x^2^
```

Index dolny: H~2~O
Index górny: x^2^

## Listy

#### Lista wypunktowana

```md
- Saletra 74.64%
- Węgiel drzewny 13.51%
- Siarka 11,85%
```

- Saletra 74.64%
- Węgiel drzewny 13.51%
- Siarka 11,85%

#### Lista numerowana

```md
1. Zebrać 100000zł
2. Zainwestować w Bitcoina
3. Znów być biednym
```

1. Zebrać 100000zł
2. Zainwestować w Bitcoina
3. Znów być biednym

#### Lista wielopoziomeowa

Można tworzyć listy wielopoziomeowe oraz łączyć rodzaje list

```md
1. Kurs programowania **Python**
    - Konfiguracja środowiska
    - Nauka podstaw
        - Zmienne i podstawowe operacje
        - Instrukcje warunkowe `if`...`else`
        - Pętle `while` oraz `for`
    - Projekt QUIZ'u z własnymi pytaniami
2. Szkolenia z dokumentów **Markdown**
    1. Poznanie elementów składni
    2. Stworzenie własnego bloga, kursu lub książki kulinarniej
```

1. Kurs programowania **Python**
    - Konfiguracja środowiska
    - Nauka podstaw
        - Zmienne i podstawowe operacje
        - Instrukcje warunkowe `if`...`else`
        - Pętle `while` oraz `for`
    - Projekt QUIZ'u z własnymi pytaniami
2. Szkolenia z dokumentów **Markdown**
    1. Poznanie elementów składni
    2. Stworzenie własnego bloga, kursu lub książki kulinarniej

### Lista zadań

```
- [x] Pójść z znajomymi na trzepak
- [ ] Nauczyć się na egzamin
- [ ] Przygotować projekt na zaliczenie
```

- [x] Pójść z znajomymi na trzepak
- [ ] Nauczyć się na egzamin
- [ ] Przygotować projekt na zaliczenie

## Definicje

Do objaśniania terminów oraz formułowania definicji została opracowana specjalna składnia.

```
Dzban
: Potoczne określenie w języku polskim, funkcjonujące zwłaszcza w mowie młodzieżowej, oznaczające głupka lub kogoś, kto zrobił coś głupiego. Epitet ten ma charakter wieloznaczny i przypisuje się mu różne skojarzenia. Wzrost popularności tego określenia został zaobserwowany w roku 2018.
```

Dzban
: Potoczne określenie w języku polskim, funkcjonujące zwłaszcza w mowie młodzieżowej, oznaczające głupka lub kogoś, kto zrobił coś głupiego. Epitet ten ma charakter wieloznaczny i przypisuje się mu różne skojarzenia. Wzrost popularności tego określenia został zaobserwowany w roku 2018.

## Przypisy

Gdy chcemy w tekście wskazywać na terminy i zwroty, które zostaną wyjaśnione na dole dokumentu, możemy zastosować składnię `[^x]`, gdzie `x` jest numerem przypisu.

```
**Język C** ujrzał światło dzienne w 1972 roku i pomimo zaawansowanego wieku wciąż jest powszechnie używany.
Na rynku istnieje oczywiście wiele innych języków, zazwyczaj łatwiejszych dla programistów,
jednak C wciąż nie ma sobie równych w wielu zastosowaniach [^1].

[^1]: _Język C - Programowanie dla początkujących_, Greg Perry, Dean Miller, 2013
```

**Język C** ujrzał światło dzienne w 1972 roku i pomimo zaawansowanego wieku wciąż jest powszechnie używany.
Na rynku istnieje oczywiście wiele innych języków, zazwyczaj łatwiejszych dla programistów,
jednak C wciąż nie ma sobie równych w wielu zastosowaniach [^1].

[^1]: _Język C - Programowanie dla początkujących_, Greg Perry, Dean Miller, 2013

## Linki

Aby przenieść się do innego dokumentu/pliku, należy stworzyć **hiperłącze**. Może ono prowadzić zarówno do dokumentów lub innych plików znajdujących się lokalnie w folderze z dokumentem, jak i do zawartości dostępnej w internecie. W składni obie opcje się nie różnią, jedynie adres/ścieżka mają inną postać.

```
[Link do pliku lokalnego](./path/to/file.md)
[Link do pliku w internecie](https://some-website.com)
[Link do nagłówka w tym pliku](#some-header)
```

[Link do pliku lokalnego](./aux-file.md)
[Link do pliku w internecie](https://google.com)
[Link do nagłówka w tym pliku](#nagłówki)

Jeżeli chcemy, aby zawartość dokumentu lub pliku znalazła się w tym dokumencie _(została do niego skopiowana)_, wystarczy przed linkiem wstawić znak `!`.

```
![Zawartość pliku lokalnego](./aux-file.md)
![Link do pliku w internecie](https://google.com)
```

![Zawartość pliku lokalnego](./aux-file.md)

### Obrazy

Wstawianie zawartości z określonej ścieżki jest doskonałym sposobem na wyświetlanie grafik. Podobnie jak w przypadku linków, obrazy mogą być umieszczone lokalnie w folderze z dokumentem lub pobierane z internetu.

```
![Obraz z rozszerzeniem PNG](./path/to/image.png)
```

![Logo Markdown](./logo-markdown.png)

### Tabele

Cechą języka Markdown jest to, że kod sam w sobie ma jak najbardziej przypominać oryginalny dokument, dzięki czemu nawet bez konwertera, który przekształci go w ładny sposób, dokument jest stosunkowo czytelny. Szczególnie wyraźne staje się to podczas tworzenia w nim tabel, które budujemy ze znaków `|`, `-` i `:`, z których ostatni wskazujemy na wyrównanie.

```
|  Lp   | Państwo           | Powierzchnia | Liczba mieszkańców |
| :---: | :---------------- | -----------: | -----------------: |
|   1   | Rosja             |   17 098 242 |        146 238 185 |
|   2   | Kanada            |    9 984 670 |         37 943 231 |
|   3   | Chiny             |    9 596 960 |        332 403 650 |
|   4   | Stany Zjednoczone |    9 525 067 |      1 411 778 724 |
|   5   | Brazylia          |    8 515 767 |        217 240 060 |
```

Największe państwa świata:

|  Lp   | Państwo           | Powierzchnia | Liczba mieszkańców |
| :---: | :---------------- | -----------: | -----------------: |
|   1   | Rosja             |   17 098 242 |        146 238 185 |
|   2   | Kanada            |    9 984 670 |         37 943 231 |
|   3   | Chiny             |    9 596 960 |        332 403 650 |
|   4   | Stany Zjednoczone |    9 525 067 |      1 411 778 724 |
|   5   | Brazylia          |    8 515 767 |        217 240 060 |

## Blok kodu

Na początku Markdown został stworzony jako narzędzie do tworzenia dokumentacji dla programistów, więc nie powinno być zaskoczeniem, że wspiera umieszczanie bloków kodu wraz z kolorowaniem składni dla wielu technologii. Fragment kodu należy umieścić między tagami ` ``` ` oraz można wskazać język, w którym został napisany kod, ale nie trzeba.

#### Blok kodu w języku Python

```
```py
a = "5"
b = 10
c = a + str(b) # łączenie str'ingów
print(c)
d = b + int(a) # dodawanie int'ów
print(d)
```
```

```py
a = "5"
b = 10
c = a + str(b) # łączenie str'ingów
print(c)
d = b + int(a) # dodawanie int'ów
print(d)
```

## Emoji

Emotikony możemy kopiwać _(np. [stąd](https://pl.piliapp.com/emoji/list/))_ i umieszczać bezpośrednio w dokumencie, jak również możemy stosować ich kody.

```
👍 + :heart:
```

👍 + :heart:

## Projekt

Projekt obejmuje stworzenie własnego dokumentu/projektu w technologii **Markdown**, który będzie stanowić:

- **Tutoriala** obejmującego wybraną tematykę, składającego się z strony tytułowej oraz co najmniej trzech lekcji.
- **Książka kucharska** z stroną tytułową o gotowaniu i dietetyce z trzema przepisami.
- **Przewodnik turystyczny** po wybranym mieście lnnej lokacji, z ogólnym opisem oraz trzema najciekawszymi miejscówkami.
- **Blog** składający się ze strony tytułowej o nas lub fikcyjnej postaci, wraz z trzema wpisami.

Minimalne wymagania projektowe:

- [ ] Każdy projekt/dokument musi składać się z **pliku głównego** `readme.md` oraz przynajmniej **trzech plików dodatkowych** `.md`.
- [ ] Muszą być stosowane [wyróżnienia](#wyróżnianie-tekstu) w tekście w sposób spójny.
- [ ] Każda strona/plik dokumentu musi zawierać przynajmniej **jedną grafikę**/obraz _(grafiki muszą być umieszczone lokalnie w projekcie)_.
- [ ] Projekt w całości musi zawierać przynajmniej **dwie listy** wypunktowane/numerowane 
- [ ] Projekt musi zawierać przynajmniej **jedną tabelę**.
- [ ] Projekt musi zawierać przynajmniej **jeden link** zewnętrzny.
