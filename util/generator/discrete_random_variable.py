__author__ = 'Alexey'
from math import ceil, log
from util.generator.base_random_variable import builtin_generator


def geometric(n, p):
    base_sequence = builtin_generator(n)
    return [ceil(log(x) / log(1 - p) - 1) for x in base_sequence]


def negative_binomial(n, p, r):
    base_sequence = builtin_generator(n)
    if len(base_sequence) % r != 0:
        print 'Base sequence length does not match passed r parameter.'
        return None
    geometric_seq = geometric(base_sequence, p)
    return [sum(geometric_seq[i:i + r]) for i in range(0, len(geometric_seq), r)]
