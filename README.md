## Wymagania
Kod służący do przeprowadzenia dowodu oraz generowania danych został napisany w języku C++ i z kompilatorem g++ (GCC) w wersji 15.1.1.
Wykorzystuje bibliotekę CAPD w wersji 6.0.0 (https://capd.ii.uj.edu.pl/), zbudowaną ze źródeł.
Programy do generowania wykresów zostały napisane w języku Python w wersji 3.13.3.


## Instrukcje odnośnie kompilacji
W pliku Makefile należy nadpisać zmienną `capdconfig` na swoją ścieżkę do biblioteki CAPD. Następnie, aby zbudować projekt należy 
w terminalu przejść do głównego folderu projektu i wywołać komendę `make`. Wówczas wszystkie pliki z `/src/` będą gotowe do uruchomienia. Odpalamy je komendą `./nazwa-programu`

## Nawigacja po kodzie

- Implementacja funkcji związanych z odwzorowaniem Poincarégo oraz układem Rösslera
```bash
 /src/utils.cpp
 ```
- Ograniczenie dolne: 
```bash
 /src/lower-bound.cpp
```
- Ograniczenie górne: 
```bash
/src/upper-bound.cpp
```
- Generowanie punktów dla diagramu bifurkacyjnego: 
```bash
/src/poincare-bifurcation-diagram.cpp
```
