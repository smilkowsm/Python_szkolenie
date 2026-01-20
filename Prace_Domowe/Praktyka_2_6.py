# Praktyka 2.6

# Zadanie 1
# Wypisz tabliczkę mnożenia dla liczby zdefiniowanej przez użytkownika. Jeśli użytkownik wpisał 7, wynik powinien wyglądać następująco:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# ...

liczba = int(input("Podaj liczbe: "))
for i in range(1, 10):
    print(f"{liczba} * {i} = {liczba * i}")
    

# Zadanie 2
# Napisz program przeliczający waluty. Zaimplementuj dialog z użytkownikiem poprzez menu.

waluta = input("Jaka walute chcesz przeliczyc? (PLN, USD, EUR): ")
PLN_to_EUR = waluta * 0.24
PLN_to_USD = waluta * 0.28
EUR_to_PLN = waluta * 4.23
EUR_to_USD = waluta * 1.18
USD_to_PLN = waluta * 3.59
USD_to_EUR = waluta * 0.85


# Zadanie 3
# Użytkownik wpisuje punkt początkowy i końcowy zakresu oraz liczbę. Jeśli liczba nie mieści się w zakresie, program prosi użytkownika o ponowne wprowadzenie liczby i tak dalej, aż użytkownik wprowadzi liczbę poprawnie. 
# Program wyświetla wszystkie liczby w zakresie, podświetlając liczbę wykrzyknikiem. Na przykład: 1 2 3 !4! 5 6 7.



# Zadanie 4
# Opracuj grę Zgadnij liczbę. Program wybiera liczbę z zakresu od 1 do 500. Użytkownik próbuje ją odgadnąć. Po każdej próbie program podpowiada, czy liczba jest większa czy mniejsza od odgadniętej. 
# Na koniec program wyświetla statystyki: ile prób zajęło odgadnięcie liczby, jak długo to trwało. Umożliwia wyjście przez wpisanie 0, jeśli użytkownik jest zmęczony zgadywaniem liczby.


