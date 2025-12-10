import numpy as np
import matplotlib.pyplot as plt

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

def run_test(title, t_nodes, y_nodes, true_func=None):
    S, z = cubic_spline(t_nodes, y_nodes)
    
    x_dense = np.linspace(t_nodes[0], t_nodes[-1], 300)
    y_spline = [S(x) for x in x_dense]
    
    plt.figure(figsize=(10, 8))
    
    if true_func:
        y_true = [true_func(np.clip(x, t_nodes[0], t_nodes[-1])) for x in x_dense]
        plt.plot(x_dense, y_true, color='#377eb8', linestyle='--', linewidth=1.5, label='Rzeczywista funkcja', alpha=0.7)
        
    plt.plot(x_dense, y_spline, color='#377eb8', linestyle='-', linewidth=2.5, label='Funkcja sklejana')
    
    plt.plot(t_nodes, y_nodes, color="#26567d", marker='o', linestyle='', markersize=8, label='Węzły', zorder=5)

    plt.grid(which='major', color='#DDDDDD', linewidth=1.2)
    plt.minorticks_on()
    plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.8)
    
    plt.axis('equal')

    plt.title(title, fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('t', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend(loc='upper right', framealpha=1.0)
    
    plt.show()

    print(f"--- {title} ---")
    print(f"Węzły: {t_nodes}")
    print(f"Obliczona wartość 'z' (2 pochodna) w punktach: {[round(val, 4) for val in z]}\n")

# Przykład 1: Funkcja sin(x) w przedziale [0, 2pi] z 4 węzłami równo rozłożonymi
t1 = np.linspace(0, 2*np.pi, 4) 
y1 = np.sin(t1)
run_test("Funkcja $\sin(t)$ z węzłami równo rozłożonymi", t1, y1, np.sin)

# Przykład 2: Funkcja sqrt(x) w przedziale [0, 2.25] z 10 węzłami równo rozłożonymi
t2 = np.linspace(0, 2.25, 10)
y2 = [np.sqrt(val) for val in t2]
run_test("Funkcja $\sqrt{t}$ z węzłami równo rozłożonymi", t2, y2, np.sqrt)

# Przykład 2: Funkcja sqrt(x) w przedziale [0, 2.25] z 10 węzłami nierówno rozłożonymi
t3 = [0, 0.1, 0.2, 0.4, 0.9, 1.3, 1.7, 1.8, 2, 2.25]
y3 = [np.sqrt(val) for val in t3]
run_test("Funkcja $\sqrt{t}$ z węzłami nierówno rozłożonymi", t3, y3, np.sqrt)