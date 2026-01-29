import numpy as np

def przewodnictwo_cieplne(h, k, M):
    """
    Jawny schemat metody różnic skończonych dla równania ciepła
    u[t] = u[xx], gdzie 0 < x < 1, t > 0
    u(x,0) = sin(pi x)
    u(0,t) = u(1,t) = 0
    """

    # parametry siatki
    n = int(1 / h) - 1
    s = k / h**2

    # siatka przestrzenna
    x = np.linspace(0.0, 1.0, n + 2)

    # warunek początkowy i warunki brzegowe
    def u(x):
        return np.sin(np.pi * x)

    def a(t):
        return 0.0

    def b(t):
        return 0.0

    def exact(x, t):
        return np.exp(-np.pi**2 * t) * np.sin(np.pi * x)

    # inicjalizacja (w[i] ← u(ih))
    w = np.zeros(n + 2)
    for i in range(n + 2):
        w[i] = u(x[i])

    t = 0.0

    # pętla czasowa
    for j in range(1, M + 1):
        t = j * k

        v = np.zeros(n + 2)

        # warunki brzegowe
        v[0] = a(t)
        v[n + 1] = b(t)

        # punkty wewnętrzne
        for i in range(1, n + 1):
            v[i] = (
                s * w[i - 1]
                + (1 - 2 * s) * w[i]
                + s * w[i + 1]
            )

        # przepisanie v → w
        for i in range(n + 2):
            w[i] = v[i]

    # porównanie z rozwiązaniem dokładnym
    u_exact = exact(x, t)
    error_inf = np.max(np.abs(w - u_exact))

    return {
        "x": x,
        "u_numeric": w,
        "u_exact": u_exact,
        "t_final": t,
        "s": s,
        "error_inf": error_inf,
    }

result = przewodnictwo_cieplne(
    h=0.1,
    k=0.005125,
    M=200
)

print("t końcowe =", result["t_final"])
print("s =", result["s"])
print("|błąd| =", result["error_inf"])

result = przewodnictwo_cieplne(
    h=0.1,
    k=0.006,
    M=171
)

print("t końcowe =", result["t_final"])
print("s =", result["s"])
print("|błąd| =", result["error_inf"])