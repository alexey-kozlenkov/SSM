from lab2.function import build_exact_negative_binomial_density, build_exact_negative_binomial_distribution_function, \
    build_empiric_distribution_function
from util.generator.discrete_random_variable import negative_binomial
from util.plotter import plot_histogram_with_exact_function, plot_two_functions
from util.utils import get_average_and_dispersion

p = 0.5
r = 5
N = 1000

negative_binomial_sequence = negative_binomial(r * N, p, r)

k = int(max(negative_binomial_sequence))
exact_negative_binomial_density = build_exact_negative_binomial_density(p, r, n=k)
plot_histogram_with_exact_function(negative_binomial_sequence, k, exact_negative_binomial_density[1],
                                   'Exact negative binomial distribution', 'lab2/negative_binomial_seq',
                                   title='Negative binomial distribution')

n = int(max(negative_binomial_sequence))
exact_negative_binomial_density_function = build_exact_negative_binomial_distribution_function(p, r, n)
empiric_negative_binomial_distribution_function = build_empiric_distribution_function(negative_binomial_sequence, n)
plot_two_functions(exact_negative_binomial_density_function[0], exact_negative_binomial_density_function[1],
                   'Exact distr. function',
                   empiric_negative_binomial_distribution_function[0],
                   empiric_negative_binomial_distribution_function[1],
                   'Empiric distr. function',
                   'lab2/negative_binomial_distribution_functions', 'Negative binomial distribution functions')

average, dispersion = get_average_and_dispersion(negative_binomial_sequence)
print('Negative binomial distribution:')
print(('\tExpected average: ', average, ', expected dispersion: ', dispersion))
print(('\tExact average: ', r * (1 - p) / p, ', exact dispersion: ', r * (1 - p) / p ** 2))
