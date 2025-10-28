import numpy as np
import math

def newton_method(f, df, x0, delta=1e-7, epsilon=1e-7, max_iter=100, n=0):
    fx = f(x0)
    dfx = df(x0)

    if dfx == 0:
        raise ValueError(f"Pochodna równa zero w x = {x0}. Brak zbieżności.")

    x1 = x0 - fx / dfx
    print(f"Iteracja {n + 1}: x = {x1}")

    if abs(x1 - x0) < delta or abs(f(x1)) < epsilon:
        return x1, n + 1

    if n >= max_iter:
        raise ValueError("Przekroczono max_iter. Brak zbieżności.")

    return newton_method(f, df, x1, delta, epsilon, max_iter, n + 1)

def secant_method(f, x0, x1, delta=1e-7, epsilon=1e-7, max_iter=100, n=0):
    f0 = f(x0)
    f1 = f(x1)

    if f1 - f0 == 0:
        raise ValueError(f"Dzielenie przez 0 w {n} iteracji. Brak zbieżności.")

    x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
    print(f"Iteracja {n + 1}: x = {x2}")

    if abs(x2 - x1) < delta or abs(f(x2)) < epsilon:
        return x2, n + 1

    if n >= max_iter:
        raise ValueError("Przekroczono max_iter. Brak zbieżności.")

    return secant_method(f, x1, x2, delta, epsilon, max_iter, n + 1)

def bisection_method(f, a, b, delta=1e-6, epsilon=1e-6, max_iter=100):
    u = f(a)
    v = f(b)
    e = b - a

    if np.sign(u) == np.sign(v):
        raise ValueError("f(a) i f(b) muszą mieć przeciwne znaki.")

    for k in range(1, max_iter + 1):
        e = e / 2
        c = a + e
        w = f(c)

        print(f"Iteracja {k}: x = {c}")

        if abs(e) < delta or abs(w) < epsilon:
            return c, k

        if np.sign(u) != np.sign(w):
            b = c 
            v = w
        else:
            a = c
            u = w

    raise ValueError("Przekroczono max_iter. Brak zbieżności.")


f1 = lambda x: x**2 - 2
df1 = lambda x: 2*x

f2 = lambda x: math.cos(x) - x
df2 = lambda x: -math.sin(x) - 1

f3 = lambda x: math.exp(-x) - x
df3 = lambda x: -math.exp(-x) - 1

f4 = lambda x: x**3 - 3*x + 2
df4 = lambda x: 3*(x**2) - 3

f5 = lambda x: x**3 - 2*x + 2
df5 = lambda x: 3*(x**2) - 2



root, iterations = newton_method(f5, df5, x0=2.0)
print(f"x0 ≈ {root:.7f}, wyznaczone w {iterations} iteracjach.\n")

root, iterations = secant_method(f5, x0=0.0, x1=2.0)
print(f"x0 ≈ {root:.7f}, wyznaczone w {iterations} iteracjach.\n")

root, iterations = bisection_method(f5, a=-3.0, b=1.0)
print(f"x0 ≈ {root:.7f}, wyznaczone w {iterations} iteracjach.")