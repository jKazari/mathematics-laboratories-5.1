import numpy as np

def cubic_spline(t, y):
    """
    Wejście:
        t - lista punktów t_i (x)
        y - lista wartości y_i (y)
    Wyjście:
        funkcja spline(x) zwracająca wartość funkcji sklejanej oraz tablice h, z (druga pochodna)
    """

    n = len(t) - 1                     # n+1 punktów -> n przedziałów
    h = [t[i+1] - t[i] for i in range(n)]
    b = [6*(y[i+1] - y[i])/h[i] for i in range(n)]

    # Rozwiązywanie układu trójprzekątniowego
    u = [0]*(n+1)
    v = [0]*(n+1)
    z = [0]*(n+1)

    # z0 = zn = 0 zostaje automatycznie

    u[1] = 2*(h[0] + h[1])
    v[1] = b[1] - b[0]

    for i in range(2, n):
        u[i] = 2*(h[i-1] + h[i]) - (h[i-1]**2)/u[i-1]
        v[i] = b[i] - b[i-1] - (h[i-1]*v[i-1])/u[i-1]

    for i in range(n-1, 0, -1):
        z[i] = (v[i] - h[i]*z[i+1]) / u[i]

    z[0] = 0
    z[n] = 0

    # Funkcja zwracająca wartość funkcji sklejanej w punkcie x
    def spline(x):
        if x < t[0] or x > t[n]:
            raise ValueError("x poza zakresem danych.")

        i = max(0, min(n-1, next(j for j in range(n) if t[j] <= x <= t[j+1])))

        hi = h[i]
        A = (t[i+1] - x)/hi
        B = (x - t[i])/hi

        S = (z[i]/6*(t[i+1]-x)**3 + z[i+1]/6*(x-t[i])**3)/hi \
            + (y[i+1]/hi - z[i+1]*hi/6)*(x - t[i]) \
            + (y[i]/hi - z[i]*hi/6)*(t[i+1]-x)

        return S

    return spline, z

t = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
y = [np.sqrt(i) for i in t]

f, z = cubic_spline(t, y)

print("Druga pochodna w punktach:")
for i in z:
    print(i)
print("Wartość funkcji sklejanej w x = 1.5:", f(1.5))