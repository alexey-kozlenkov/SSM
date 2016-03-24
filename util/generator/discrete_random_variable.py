__author__ = 'Alexey'
from math import ceil, log


def geometric(base_sequence, p):
    return map(lambda x: ceil(log(x) / log(1 - p) - 1), base_sequence)
