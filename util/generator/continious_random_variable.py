from math import sqrt, log, tan, pi

__author__ = 'Alexey'
from base_random_variable import builtin_generator


def normal(average, dispersion, n, N=12):
    standard = normal_standard(n, N)
    return [average - x * sqrt(dispersion) for x in standard]


def normal_standard(n, N=12):
    base_sequences = [builtin_generator(n) for i in range(N)]
    return [sqrt(12. / N) * (sum(base[i] for base in base_sequences) - N / 2.) for i in range(n)]


def exponential(l, n):
    base_sequence = builtin_generator(n)
    return [-log(x) / l for x in base_sequence]


def cauchy(m, c, n):
    base_sequence = builtin_generator(n)
    return [m + c * tan(pi * (a - 0.5)) for a in base_sequence]


def mixed(n, p, first_distribution, second_distribution):
    base_sequence = builtin_generator(n)
    return [first_distribution[i] if base_sequence[i] < p else second_distribution[i] for i in range(n)]


def normal_standard_by_box_muller(n):
    first_sequence = builtin_generator(n, -1, 1)
    second_sequence = builtin_generator(n, -1, 1)
    first_result = []
    second_result = []
    for x, y in zip(first_sequence, second_sequence):
        s = x ** 2 + y ** 2
        if s and s <= 1:
            first_result.append(x * sqrt(-2 * log(s) / s))
            second_result.append(y * sqrt(-2 * log(s) / s))
    return first_result, second_result
