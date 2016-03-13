__author__ = 'Alexey'
from lab1.data import mcg_data
from util.generator.base_random_variable import multiplicative_congruential_generator
from util.generator.discrete_random_variable import geometric

p = 0.7

base_sequence = multiplicative_congruential_generator(mcg_data.a0, mcg_data.M, mcg_data.beta, mcg_data.n)
geometric_seq = geometric(base_sequence, p)

average = sum(geometric_seq) / len(geometric_seq)
dispersion = sum((x - average) ** 2 for x in geometric_seq) / (len(geometric_seq) - 1)
print 'Expected average: ', average, ', expected dispersion: ', dispersion
print 'Exact average: ', 1. / p, ', exact dispersion: ', (1 - p) / p ** 2
