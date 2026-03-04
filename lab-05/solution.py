import math

# 1. Implementacja metod

def metoda_trapezow(f, a, b, n):
    
    # a, b: granice całkowania
    # n: liczba podprzedziałów
    
    h = (b - a) / n
    suma = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        x = a + i * h
        suma += f(x)
        
    return suma * h

def metoda_simpsona(f, a, b, n):

    # n musi być parzyste (n = 2m).
    
    if n % 2 != 0:
        raise ValueError("Metoda Simpsona wymaga parzystej liczby przedziałów (n).")
        
    h = (b - a) / n
    suma = f(a) + f(b)  # f0 + f2m
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            suma += 2 * f(x)
        else:
            suma += 4 * f(x)
            
    return (h / 3) * suma

# 2. Definicja funkcji testowych i ich dokładnych całek

def f1(x): return x**2
def f1_calka_dokladna(a, b): return (b**3)/3 - (a**3)/3

def f2(x): return math.sin(x)
def f2_calka_dokladna(a, b): return -math.cos(b) - (-math.cos(a))

def f3(x): return math.exp(x)
def f3_calka_dokladna(a, b): return math.exp(b) - math.exp(a)

# 3. Eksperymenty

def przeprowadz_eksperyment():
    
    testy = [
        (f1, f1_calka_dokladna, 0, 1, "f(x) = x^2, [0, 1]"),
        (f2, f2_calka_dokladna, 0, math.pi, "f(x) = sin(x), [0, PI]"),
        (f3, f3_calka_dokladna, 0, 1, "f(x) = e^x, [0, 1]")
    ]
    
    kroki_n = [2, 4, 10, 20, 100, 1000, 100000] 

    print(f"{'Metoda':<15} | {'N':<8} | {'Wynik':<15} | {'Dokładna':<15} | {'Błąd bezwzg.':<15}")
    print("-" * 80)

    for f, f_dokladna, a, b, opis in testy:
        print(f"\nFunkcja: {opis}")
        print("-" * 80)
        wartosc_dokladna = f_dokladna(a, b)
        
        for n in kroki_n:
            
            wynik_trap = metoda_trapezow(f, a, b, n)
            blad_trap = abs(wynik_trap - wartosc_dokladna)
            
            wynik_simp = metoda_simpsona(f, a, b, n)
            blad_simp = abs(wynik_simp - wartosc_dokladna)
            
            print(f"{'Trapezów':<15} | {n:<8} | {wynik_trap:<15.8f} | {wartosc_dokladna:<15.8f} | {blad_trap:<15.8e}")
            print(f"{'Simpsona':<15} | {n:<8} | {wynik_simp:<15.8f} | {wartosc_dokladna:<15.8f} | {blad_simp:<15.8e}")
            print("-" * 40)

if __name__ == "__main__":
    przeprowadz_eksperyment()