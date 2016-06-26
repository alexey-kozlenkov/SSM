from lab2.function import build_exact_geometric_density, build_empiric_distribution_function, \
    build_exact_geometric_distribution_function
from util.generator.discrete_random_variable import geometric
from util.plotter import plot_histogram_with_exact_function, plot_two_functions
from util.utils import get_average_and_dispersion

N = 1000
p = 0.7

geometric_seq = geometric(N, p)

k = int(max(geometric_seq))
exact_geometric_density = build_exact_geometric_density(p, n=k)
plot_histogram_with_exact_function(geometric_seq, k, exact_geometric_density[1], 'Exact geometric distribution',
                                   'lab2/geometric_seq', title='Geometric distribution')

n = int(max(geometric_seq))
exact_geometric_distribution_function = build_exact_geometric_distribution_function(p, n)
empiric_geometric_distribution_function = build_empiric_distribution_function(geometric_seq, n)
plot_two_functions(exact_geometric_distribution_function[0], exact_geometric_distribution_function[1],
                   'Exact distr. function',
                   empiric_geometric_distribution_function[0], empiric_geometric_distribution_function[1],
                   'Empiric distr. function',
                   'lab2/geometric_distribution_functions', 'Geometric distribution functions')

average, dispersion = get_average_and_dispersion(geometric_seq)
print('Geometric distribution:')
print(('\tExpected average: ', average, ', expected dispersion: ', dispersion))
print(('\tExact average: ', (1 - p) / p, ', exact dispersion: ', (1 - p) / p ** 2))
