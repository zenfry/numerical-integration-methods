import math


def f1(x):
    return x ** 2


def f1_exact(a, b):
    return (b ** 3 - a ** 3) / 3


def f2(x):
    return math.sin(x)


def f2_exact(a, b):
    return -math.cos(b) + math.cos(a)


def f3(x):
    return math.exp(-x ** 2)


def f3_reference(a, b):
    return (math.sqrt(math.pi) / 2) * (math.erf(b) - math.erf(a))


def riemann_sum(f, a, b, n, kind="midpoint"):
    h = (b - a) / n
    total = 0.0

    for i in range(n):
        x_left = a + i * h
        if kind == "left":
            sample_x = x_left
        elif kind == "right":
            sample_x = x_left + h
        elif kind == "midpoint":
            sample_x = x_left + h / 2
        else:
            raise ValueError("kind must be 'left', 'right', or 'midpoint'")
        total += f(sample_x) * h

    return total


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x_i = a + i * h
        total += f(x_i)

    return total * h


def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson's rule requires an even number of intervals")

    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        coefficient = 4 if i % 2 != 0 else 2
        total += coefficient * f(x_i)

    return total * h / 3


def compare_methods(f, a, b, exact_value, label, n_values=(4, 8, 16, 32, 64)):
    print(f"\n=== {label} on [{a}, {b}] ===")
    print(f"{'n':>4} | {'Midpoint':>12} | {'Trapezoid':>12} | {'Simpson':>12} | "
          f"{'Simp. Error':>12}")
    print("-" * 62)

    for n in n_values:
        mid = riemann_sum(f, a, b, n, kind="midpoint")
        trap = trapezoidal_rule(f, a, b, n)
        simp = simpsons_rule(f, a, b, n)
        simp_error = abs(simp - exact_value)

        print(f"{n:>4} | {mid:12.6f} | {trap:12.6f} | {simp:12.6f} | "
              f"{simp_error:12.2e}")

    print(f"{'exact':>4} | {'':>12} | {'':>12} | {exact_value:12.6f} |")


if __name__ == "__main__":
    compare_methods(f1, 0, 2, f1_exact(0, 2), "f(x) = x^2")

    compare_methods(f2, 0, math.pi, f2_exact(0, math.pi), "f(x) = sin(x)")

    compare_methods(f3, 0, 1, f3_reference(0, 1),
                     "f(x) = e^(-x^2)  [no closed-form antiderivative]")
