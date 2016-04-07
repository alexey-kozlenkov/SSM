__author__ = 'Alexey'
from numpy.random import uniform


def multiplicative_congruential_generator(start, module, multiplier, n):
    result = [float(start) / module]
    values = [start]
    for i in range(1, n + 1):
        previous = values[i - 1]
        current = previous * multiplier % module
        values.append(current)
        result.append(float(current) / module)
    return result[1:]


def maclaren_marsaglia_generator(sequence_1, sequence_2, k, n):
    v = [sequence_1[i] for i in range(k)]
    result = []
    for i in range(n):
        index = int(sequence_2[i] * k)
        result.append(v[index])
        v[index] = sequence_1[i + k]
    return result


def builtin_generator(n, a=0, b=1):
    return uniform(a, b, n)
