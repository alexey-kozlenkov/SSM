__author__ = 'Alexey'
from math import sqrt, floor

from scipy.stats import chi2


def build_exact_geometric_density(p, n=1000):
    x = [i for i in range(n)]
    y = [p * (1 - p) ** i for i in x]
    return x, y


def build_exact_geometric_distribution_function(p, n=1000):
    x = [i for i in range(n)]
    y = [1 - (1 - p) ** i for i in x]
    return x, y


def build_empiric_geometric_distribution_function(sequence, n=1000):
    x = [i for i in range(n)]
    y = [float(len(filter(lambda x: x < x_i, sequence))) / len(sequence) for x_i in x]
    return x, y
