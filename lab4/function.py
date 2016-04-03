__author__ = 'Alexey'
from math import pi, sqrt, exp
from numpy import linspace


def build_exact_normal_distribution_density(average, dispersion, n=1000, left=-5, right=5):
    x = linspace(left, right, n + 1)
    s = sqrt(dispersion)
    y = [(1. / (sqrt(2 * pi) * s) * exp(-(x_i - average) ** 2 / (2 * dispersion))) for x_i in x]
    return x, y


def build_exact_exponential_distribution_density(l, n=1000, right=5):
    x = linspace(0, right, n + 1)
    y = [(l * exp(-l * x_i)) for x_i in x]
    return x, y


def build_exact_cauchy_distribution_density(m, c, n=1000, left=-5, right=5):
    x = linspace(left, right, n + 1)
    y = [1. / (pi * c * (1 + ((x_i - m) / c) ** 2)) for x_i in x]
    return x, y
