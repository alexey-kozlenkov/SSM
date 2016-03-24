__author__ = 'Alexey'
from lab2.function import build_exact_geometric_density, build_empiric_geometric_distribution_function, \
    build_exact_geometric_distribution_function
from util.plotter import plot_histogram_with_exact_function, plot_two_functions
from lab1.data import mcg_data
from util.generator.base_random_variable import multiplicative_congruential_generator
from util.generator.discrete_random_variable import geometric

p = 0.7

base_sequence = multiplicative_congruential_generator(mcg_data.a0, mcg_data.M, mcg_data.beta, mcg_data.n)
geometric_seq = geometric(base_sequence, p)

k = 10
exact_geometric_density = build_exact_geometric_density(p, n=k)
plot_histogram_with_exact_function(geometric_seq, k, exact_geometric_density[1], 'Exact geometric distribution',
                                   'lab2/geometric_seq', title='Geometric distribution')

n = 10
exact_geometric_density_function = build_exact_geometric_distribution_function(p, n)
empiric_geometric_distribution_function = build_empiric_geometric_distribution_function(geometric_seq, n)
plot_two_functions(exact_geometric_density_function[0], exact_geometric_density_function[1], 'Exact distr. function',
                   empiric_geometric_distribution_function[0], empiric_geometric_distribution_function[1],
                   'Empiric distr. function',
                   'lab2/distribution_functions', 'Distribution functions')

average = sum(geometric_seq) / len(geometric_seq)
dispersion = sum((x - average) ** 2 for x in geometric_seq) / (len(geometric_seq) - 1)
print 'Geometric distribution:'
print '\tExpected average: ', average, ', expected dispersion: ', dispersion
print '\tExact average: ', (1 - p) / p, ', exact dispersion: ', (1 - p) / p ** 2
