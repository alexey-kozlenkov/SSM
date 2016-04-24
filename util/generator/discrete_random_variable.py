__author__ = 'Alexey'
from math import ceil, log
from util.generator.base_random_variable import builtin_generator


def geometric(n, p):
    base_sequence = builtin_generator(n)
    return [ceil(log(x) / log(1 - p) - 1) for x in base_sequence]


def negative_binomial(n, p, r):
    if n % r != 0:
        print 'Sequence length does not match passed r parameter.'
        return None
    geometric_seq = geometric(n, p)
    return [sum(geometric_seq[i:i + r]) for i in range(0, len(geometric_seq), r)]


def bernoulli(n, p):
    base_sequence = builtin_generator(n)
    return [0 if a < p else 1 for a in base_sequence]
