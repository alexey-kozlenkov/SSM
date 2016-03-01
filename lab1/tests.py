__author__ = 'Alexey'
from math import sqrt


def method_of_moments(sequence, boundary):
    n = len(sequence)
    average = float(sum(sequence)) / n
    dispersion = float(sum((x - average) ** 2 for x in sequence)) / (n - 1)
    c_1 = sqrt(12 * n)
    c_2 = float(n - 1) / n * pow((0.0056 / n + 0.0028 / n ** 2 - 0.0083 / n ** 3), -0.5)
    return c_1 * abs(average - 0.5) < boundary, c_2 * abs(dispersion - 1. / 12) < boundary
