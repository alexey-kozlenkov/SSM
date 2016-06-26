from math import sqrt, pi, exp, log

from scipy import integrate

from util.generator.base_random_variable import builtin_generator
from util.generator.continious_random_variable import exponential


def f1(x):
    return x ** 10 * (1 + 2 * x ** 8) ** 0.5


def f2(x):
    return 1. / (1 + x) ** 3


def f3(x, y):
    return log(1 / sqrt(x ** 2 + y ** 2))


def f3_polar(r):
    return r * log(1. / r)


print('Computing first integral...')
a, b, N = 0., 1., 1707  # All hail Comte de Buffon!

base_sequence = builtin_generator(N, a, b)
f_values = [f1(x) for x in base_sequence]
monte_carlo_value = float(b - a) / N * sum(f_values)
exact_value = integrate.quad(f1, 0, 1)[0]
print('\tExact (SciPy) value: {:.5f} VS Monte-Carlo value: {:.5f}'.format(exact_value, monte_carlo_value))

print('Computing second integral...')
lmbda = 1.
p_eta = lambda x: lmbda * exp(-lmbda * x) if x >= 0 else 0
eta_values = exponential(lmbda, N)
monte_carlo_value = sum(f2(x) / p_eta(x) for x in eta_values) / N
exact_value = integrate.quad(f2, 0, float('inf'))[0]
print('\tExact (SciPy) value: {:.5f} VS Monte-Carlo value: {:.5f}'.format(exact_value, monte_carlo_value))

print('Computing third integral...')
radius = 2
base_sequence = builtin_generator(N, 0, radius)
f_values = [f3_polar(r) for r in base_sequence]
monte_carlo_value = 2 * pi * float(radius) / N * sum(f_values)
exact_value = 2 * pi * integrate.quad(lambda r: r * log(1. / r), 0, radius)[0]
print('\tExact (SciPy) value: {:.5f} VS Monte-Carlo value: {:.5f}'.format(exact_value, monte_carlo_value))
