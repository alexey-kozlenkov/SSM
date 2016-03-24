__author__ = 'Alexey'
from scipy.special import comb, betainc


def build_exact_geometric_density(p, n=1000):
    x = [i for i in range(n)]
    y = [p * (1 - p) ** i for i in x]
    return x, y


def build_exact_negative_binomial_density(p, r, n=1000):
    x = [i for i in range(n)]
    y = [comb(x_i + r - 1, x_i, exact=True) * (p ** r) * ((1 - p) ** x_i) for x_i in x]
    return x, y


def build_exact_geometric_distribution_function(p, n=1000):
    x = [i for i in range(n)]
    y = [1 - (1 - p) ** i for i in x]
    return x, y


def build_exact_negative_binomial_distribution_function(p, r, n=1000):
    x = [i for i in range(n)]
    y = [betainc(r, x_i + 1, p) for x_i in x]
    return x, y


def build_empiric_distribution_function(sequence, n=1000):
    x = [i for i in range(n)]
    y = [float(len(filter(lambda x: x < x_i, sequence))) / len(sequence) for x_i in x]
    return x, y
