from lab2.function import build_exact_negative_binomial_density, build_exact_negative_binomial_distribution_function, \
    build_empiric_distribution_function
from util.plotter import plot_histogram_with_exact_function, plot_two_functions

__author__ = 'Alexey'

from lab1.data import mcg_data
from util.generator.base_random_variable import multiplicative_congruential_generator
from util.generator.discrete_random_variable import negative_binomial

p = 0.5
r = 5
N = 1000

base_sequence = multiplicative_congruential_generator(mcg_data.a0, mcg_data.M, mcg_data.beta, r * N)
negative_binomial_sequence = negative_binomial(base_sequence, p, r)

k = 25
exact_negative_binomial_density = build_exact_negative_binomial_density(p, r, n=k)
plot_histogram_with_exact_function(negative_binomial_sequence, k, exact_negative_binomial_density[1],
                                   'Exact negative binomial distribution', 'lab2/negative_binomial_seq',
                                   title='Negative binomial distribution')

k = 25
exact_negative_binomial_density_function = build_exact_negative_binomial_distribution_function(p, r, k)
empiric_negative_binomial_distribution_function = build_empiric_distribution_function(negative_binomial_sequence, k)
plot_two_functions(exact_negative_binomial_density_function[0], exact_negative_binomial_density_function[1], 'Exact distr. function',
                   empiric_negative_binomial_distribution_function[0], empiric_negative_binomial_distribution_function[1],
                   'Empiric distr. function',
                   'lab2/negative_binomial_distribution_functions', 'Negative binomial distribution functions')

average = sum(negative_binomial_sequence) / N
dispersion = sum((x - average) ** 2 for x in negative_binomial_sequence) / (N - 1)
print 'Negative binomial distribution:'
print '\tExpected average: ', average, ', expected dispersion: ', dispersion
print '\tExact average: ', r * (1 - p) / p, ', exact dispersion: ', r * (1 - p) / p ** 2
