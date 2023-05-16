# Program obliczajacy calke oznaczana funkcji trzema metodami. ver 1.0 17/04/2023
import math # Importujemy math. Będziemy go używać w dalszej części programu.

def funkcja(x): # zdefiniowanie funkcji przy użyciu modułu MATH
    return log10(5 * (x ** 2) + 1) 


def metoda_prostokatow(a, b, n): # funkcja obliczająca metodą prostokątów, przyjmująca a jako początek i n jako koniec przedziału oraz n jako ilość podziałów. 
    h = (b - a) / n
    suma = 0
    for i in range(n):
        xi = a + i * h
        suma += funkcja(xi)
    return h * suma


def metoda_trapezow(a, b, n): # tak jak wyżej, jednak tym razem użyta jest metoda trapezów wraz z odpowiednim wzorem
    h = (b - a) / n
    suma = (funkcja(a) + funkcja(b)) / 2
    for i in range(1, n):
        xi = a + i * h
        suma += funkcja(xi)
    return h * suma


def metoda_simpsona(a, b, n): # metoda simpsona wraz z walidacja, czy liczba podziałów będzie parzysta lub nie
    h = (b - a) / n
    suma = funkcja(a) + funkcja(b)
    for i in range(1, n):
        xi = a + i * h
        if i % 2 == 0: # dla podziałów parzystych
            suma += 2 * funkcja(xi)
        else:
            suma += 4 * funkcja(xi) # dla podziałów niepażystych
    return (h / 3) * suma


def oblicz_calki(): # główna treść programu obliczająca całkę
    print("Program: Implementacja obliczania calki oznaczonej podanej funkcji trzema metodami")
    print("Autor: Jeremiasz Zolnierek-Kielczewski")
    while True:
        a = 0
        b = 0
        while True:
            try:
                a = float(input("Podaj wartość początkową przedziału (0 < a < b < 5): "))
                b = float(input("Podaj wartość końcową przedziału (0 < a < b < 5): "))
                if a < 0 or a >= b or b > 5: # przyjmowanie w zakresie zgodnym z informacjami z treści zadania
                    print("Podane wartości muszą spełniać warunek 0 < a < b < 5.")
                else:
                    break
            except ValueError:
                print("Wprowadzono nieprawidłową wartość.")

        while True:
            try:
                n = int(input("Podaj liczbę podziałów: ")) # wprowadzanie liczby podziałów
                if n <= 0:
                    print("Liczba podziałów musi być większa od zera.")
                else:
                    break
            except ValueError:
                print("Wprowadzono nieprawidłową wartość.")

        print("Wzór funkcji: log10(5x^2 + 1)")
        print("Metoda obliczeń: ")
        print("1 - metoda prostokątów")
        print("2 - metoda trapezów")
        print("3 - metoda Simpsona")

        while True:
            try:
                metoda = int(input("Podaj metodę obliczeń: "))
                if metoda < 1 or metoda > 3: # wybór której metody chce użyć użytkownik.
                    print("Podaj metodę obliczeń (1 - 3): ")
                else:
                    break
            except ValueError:
                print("Wprowadzono nieprawidłową wartość.")

        if metoda == 1: # przekazanie wartości do wcześniej zdefiniowanych funkcji
            wynik = metoda_prostokatow(a, b, n) 
            print("Metoda prostokątów")
        elif metoda == 2:
            wynik = metoda_trapezow(a, b, n)
            print("Metoda trapezów")
        else:
            wynik = metoda_simpsona(a, b, n)
            print("Metoda Simpsona")

        print("Liczba podziałów: ", n)
        print("Wartości krańcowe przedziału: ", a, " do ", b)
        print("Wartość obliczonej całki: ", wynik) # podanie wyniku

        while True: # mozliwość ponownego obliczenia bez ponownego uruchomienia programu
            try:
                wybor = int(input("Wybierz 0 dla zamknięcia programu, wybierz 1 aby wrócić do początku: "))
                if wybor == 0:
                    return
                elif wybor == 1:
                    break
                else:
                    print("Wybierz 0 lub 1.")
            except ValueError:
                print("Wprowadzono nieprawidłową wartość.")

oblicz_calki()
