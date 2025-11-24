import numpy as np

def back_substitution_naive(U, b):
    """
    Rozwiązuje układ Ux = b metodą podstawiania wstecz.
    Zakłada, że U jest macierzą górnotrójkątną bez zera na przekątnej.
    """
    n = U.shape[0]
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        if U[i, i] == 0:
            raise ZeroDivisionError(f"Zerowy element U[{i},{i}] na przekątnej -> metoda naiwna zawodzi.")
        suma = np.dot(U[i, i+1:], x[i+1:])
        x[i] = (b[i] - suma) / U[i, i]

    return x

def gauss_naive_solve(A, b):
    """
    Pełna, naiwna metoda Gaussa:
    - eliminacja bez skalowanego wyboru wierszy głównych
    - podstawianie wsteczne

    Zwraca:
        x – rozwiązanie układu (jeśli metoda działa)
    """
    A = A.copy().astype(float)
    b = b.copy().astype(float)
    n = A.shape[0]

    # Eliminacja
    for k in range(n - 1):
        if A[k, k] == 0:
            raise ZeroDivisionError(f"Zerowy element a[{k},{k}] -> metoda naiwna zawodzi.")
        
        for i in range(k + 1, n):
            z = A[i, k] / A[k, k]
            A[i, k] = 0.0
            
            for j in range(k + 1, n):
                A[i, j] = A[i, j] - z * A[k, j]
            b[i] -= z * b[k]

    # Podstawianie wstecz
    return back_substitution_naive(A, b)


def gaussian_scaled_elimination(A):
    """
    Eliminacja Gaussa ze skalowanym wyborem wierszy głównych. Część 1.
    
    Zwraca:
        A  – zmodyfikowana macierz (zapisane mnożniki z na miejscu)
        p  – permutacja wierszy
        s  – wektor skal
    """
    A = A.copy().astype(float)
    n = A.shape[0]
    
    # Inicjalizacja p_i i s_i
    p = np.arange(n)              # p_i <- i
    s = np.max(np.abs(A), axis=1) # s_i <- max_j |a_ij|
    
    # Główna pętla eliminacji
    for k in range(n - 1):  # k = 0,...,n-2
        # Wybór wiersza głównego wg kryterium |a[p[j],k]| / s[p[j]]
        ratios = np.abs(A[p[k:], k]) / s[p[k:]]
        j_rel = np.argmax(ratios)      # indeks względny (0...n-k-1)
        j = k + j_rel                  # indeks absolutny
        
        # Zamiana p[k] <-> p[j]
        p[k], p[j] = p[j], p[k]
        
        # Eliminacja
        for i in range(k + 1, n):
            pivot = A[p[k], k]
            if pivot == 0:
                raise ZeroDivisionError(f"Zerowy element a[p[{k}], {k}] -> nie można kontynuować.")

            z = A[p[i], k] / pivot
            A[p[i], k] = z
            
            for j in range(k + 1, n):
                A[p[i], j] -= z * A[p[k], j]

    return A, p, s

def gaussian_scaled_solve(A, p, b, return_lu = False):
    """
    Część 2 algorytmu:
    - modyfikacja wektora b z użyciem mnożników zapisanych w A
    - podstawianie wstecz z permutacją p

    Zwraca:
        x – rozwiązanie układu Ax = b
        
    Opcjonalnie zwraca macierze L, U, P
    """
    b = b.copy().astype(float)
    n = A.shape[0]

    # Eliminacja na wektorze b
    for k in range(n - 1):        # k = 0, ..., n-2
        for i in range(k + 1, n):
            b[p[i]] -= A[p[i], k] * b[p[k]]

    # Podstawianie wstecz
    x = np.zeros(n)
    for ii in range(n - 1, -1, -1):    # i = n-1 ... 0
        i = p[ii]
        suma = np.dot(A[i, ii+1:], x[ii+1:])
        x[ii] = (b[i] - suma) / A[i, ii]

    if not return_lu:
        return x

    # Wyznaczenie L, U, P
    L = np.eye(n)
    U = np.zeros_like(A)
    P = np.zeros((n, n))

    for i in range(n):
        P[i, p[i]] = 1
        for j in range(n):
            if j < i:
                L[i, j] = A[p[i], j]
            else:
                U[i, j] = A[p[i], j]

    return x, L, U, P

# Funkcje pomocnicze
def format_matrix(M):
    M = np.array(M, dtype=float)
    return "\n".join("  ".join(f"{val:10.6g}" for val in row) for row in M)

def format_vector(v):
    v = np.array(v, dtype=float)
    return "\n".join(f"{val:10.6g}" for val in v)

def try_naive_method(A, b):
    try:
        x_naive = gauss_naive_solve(A, b)
        print("Rozwiązanie naiwne:")
        print(format_vector(x_naive))
    except Exception as e:
        print("Metoda naiwna zawiodła:")
        print(" ", e)

def print_report(A, b, x, L, U, P, s, p):
    print("Dla danych macierzy A i b:")
    print("A =")
    print(format_matrix(A))
    print("\nb =")
    print(format_vector(b))

    print("\nOtrzymujemy rozwiązanie x, macierze L i U z rozkładu LU, macierz permutacji P, oraz wektor skal s i powstałą w pierwszym kroku permutację p:")
    print("\nx =")
    print(format_vector(x))

    print("\nL =")
    print(format_matrix(L))
    print("\nU =")
    print(format_matrix(U))
    print("\nP =")
    print(format_matrix(P))

    print("\ns =")
    print(s)

    print("\np =")
    print(p)

examples = [
    ("Przykład 1: dobrze uwarunkowany", 
     np.array([[2, 3, -6],
               [1, -6,  8],
               [3, -2,  1]]),
     np.array([7, 14, 28])),

    ("Przykład 2: zero na przekątnej", 
     np.array([[0, 1],
               [1, 1]]),
     np.array([1, 2])),

    ("Przykład 3: bardzo mały epsilon na przekątnej", 
     np.array([[1e-12, 1],
               [1,      1]]),
     np.array([1, 2])),

    ("Przykład 4: poprawny układ 3×3", 
     np.array([[4, -2, 1],
               [1,  6, -2],
               [3,  1,  5]]),
     np.array([1, 2, 3])),

    ("Przykład 5: układ słabo uwarunkowany", 
     np.array([[1, 1, 1],
               [1, 1.0001, 1],
               [1, 1, 1.0002]]),
     np.array([3, 3.0001, 3.0002]))
]

# Wydrukowanie rozwiązań przykładów 
for name, A, b in examples:
	print("\n" + "=" * 70)
	print(name)
	print("=" * 70)

	print("\nMetoda eliminacji Gaussa ze skalowanym wyborem wierszy głównych:")

	A2, p, s = gaussian_scaled_elimination(A)
	x, L, U, P = gaussian_scaled_solve(A2, p, b, return_lu=True)

	print_report(A, b, x, L, U, P, s, p)

	print("\nPróba rozwiązania metodą naiwną:")
	try_naive_method(A, b)

	print("\n" + "-" * 70 + "\n")