from util.generator.continious_random_variable import exponential, normal, mixed
from util.plotter import plot_histogram

__author__ = 'Alexey'

l = 0.25
m = -2
s2 = 1
n = 10000
N = 42
p = 0.8

print 'Mixed distribution'
print 'Using exponential distribution (lambda = %.3f) and normal distribution (m = %.3f, s^2 = %.3f)' % (l, m, s2)
exponential_sequence = exponential(l, n)
normal_sequence = normal(m, s2, n, N)
mixed_distribution = mixed(n, p, exponential_sequence, normal_sequence)

average = sum(mixed_distribution) / n
theoretical_average = p / l + (1 - p) * m
dispersion = sum((x - average) ** 2 for x in mixed_distribution) / (n - 1)
theoretical_dispersion = p * (1. / l ** 2 + (1. / l) ** 2) + (1 - p) * (s2 + m ** 2) - theoretical_average**2
print '\tEmpiric average: %f VS theoretical average: %f' % (average, theoretical_average)
print '\tEmpiric dispersion: %f VS theoretical dispersion: %f' % (dispersion, theoretical_dispersion)

k = 25
plot_histogram(mixed_distribution, k, 'lab4/mixed_seq', 'Mixed sequence')