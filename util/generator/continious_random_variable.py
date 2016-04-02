from math import sqrt, log

__author__ = 'Alexey'
from base_random_variable import builtin_generator


def normal(average, dispersion, n, N=12):
    standard = normal_standard(n, N)
    return map(lambda x: average - x * sqrt(dispersion), standard)


def normal_standard(n, N=12):
    base_sequences = [builtin_generator(n) for i in range(N)]
    return [sqrt(12. / N) * (sum(base[i] for base in base_sequences) - N / 2.) for i in range(n)]


def exponential(l, n):
    base_sequence = builtin_generator(n)
    return map(lambda a: -log(a) / l, base_sequence)
