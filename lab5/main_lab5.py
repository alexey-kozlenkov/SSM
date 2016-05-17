__author__ = 'Alexey'
from math import sqrt, pi, exp, log
from util.generator.base_random_variable import builtin_generator, in_circle_base_generator
from util.generator.continious_random_variable import exponential
from scipy import integrate


def f1(x):
    return x ** 10 * (1 + 2 * x ** 8) ** 0.5


def f2(x):
    return 1. / (1 + x) ** 3


def f3(x, y):
    return log(1 / sqrt(x ** 2 + y ** 2))


print 'Computing first integral...'
a, b, N = 0., 1., 1777  # All hail Comte de Buffon!

base_sequence = builtin_generator(N, a, b)
f_values = [f1(x) for x in base_sequence]
monte_carlo_value = float(b - a) / N * sum(f_values)
exact_value = integrate.quad(f1, 0, 1)[0]
print '\tExact (SciPy) value: {:.5f} VS Monte-Carlo value: {:.5f}'.format(exact_value, monte_carlo_value)

print 'Computing second integral...'
lmbda = 1.
p_eta = lambda x: lmbda * exp(- lmbda * x) if x >= 0 else 0
eta_values = exponential(lmbda, N)
monte_carlo_value = sum(f2(x) / p_eta(x) for x in eta_values) / N
exact_value = integrate.quad(f2, 0, float('inf'))[0]
print '\tExact (SciPy) value: {:.5f} VS Monte-Carlo value: {:.5f}'.format(exact_value, monte_carlo_value)
