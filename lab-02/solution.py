import numpy as np

def newton_method(f, df, x0, delta=1e-7, epsilon=1e-7, max_iter=100, n=0):
    fx = f(x0)
    dfx = df(x0)

    if dfx == 0:
        raise ValueError(f"Derivative zero at x = {x0}. No convergence.")

    x1 = x0 - fx / dfx
    print(f"Iteration {n + 1}: x = {x1}")

    if abs(x1 - x0) < delta or abs(f(x1)) < epsilon:
        return x1, n + 1

    if n >= max_iter:
        raise ValueError("Newton's method did not converge within max_iter.")

    return newton_method(f, df, x1, delta, epsilon, max_iter, n + 1)

def secant_method(f, x0, x1, delta=1e-7, epsilon=1e-7, max_iter=100, n=0):
    f0 = f(x0)
    f1 = f(x1)

    if f1 - f0 == 0:
        raise ValueError(f"Zero denominator at iteration {n}. No convergence.")

    x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
    print(f"Iteration {n + 1}: x = {x2}")

    if abs(x2 - x1) < delta or abs(f(x2)) < epsilon:
        return x2, n + 1

    if n >= max_iter:
        raise ValueError("Secant method did not converge within max_iter.")

    return secant_method(f, x1, x2, delta, epsilon, max_iter, n + 1)

def bisection_method(f, a, b, delta=1e-6, epsilon=1e-6, max_iter=100):
    u = f(a)
    v = f(b)
    e = b - a

    if np.sign(u) == np.sign(v):
        raise ValueError("f(a) and f(b) must have opposite signs.")

    for k in range(1, max_iter + 1):
        e = e / 2
        c = a + e
        w = f(c)

        print(f"Iteration {k}: x = {c}")

        # Check convergence criteria
        if abs(e) < delta or abs(w) < epsilon:
            return c, k

        # Update the interval
        if np.sign(u) != np.sign(w):
            b = c 
            v = w
        else:
            a = c
            u = w

    raise ValueError("Bisection method did not converge within max_iter iterations.")


f = lambda x: x**2 - 2
f_prime = lambda x: 2*x

root, iterations = newton_method(f, f_prime, x0=1.0)
print(f"Root ≈ {root:.7f}, found in {iterations} recursive steps.\n")

root, iterations = secant_method(f, x0=1.0, x1=2.0)
print(f"Root ≈ {root:.7f}, found in {iterations} recursive steps.\n")

root, iterations = bisection_method(f, a=1.0, b=2.0)
print(f"Root ≈ {root:.7f}, found in {iterations} iterations.")