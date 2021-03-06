from math import ceil

from lab4.function import build_exact_exponential_distribution_density
from util.generator.continious_random_variable import exponential
from util.plotter import plot_histogram_with_exact_function
from util.utils import get_average_and_dispersion

l = 0.25
n = 10000

print('Exponential distribution: lambda=%f' % l)
exponential_sequence = exponential(l, n)
average, dispersion = get_average_and_dispersion(exponential_sequence)
print('\tEmpiric average: %f VS theoretical average: %f' % (average, 1. / l))
print('\tEmpiric dispersion: %f VS theoretical dispersion: %f' % (dispersion, 1. / l ** 2))

range_bound = ceil(max(list(map(abs, exponential_sequence))))
k = 40
exact_exponential_distribution_density = build_exact_exponential_distribution_density(l, n, range_bound)
plot_histogram_with_exact_function(exponential_sequence, k, exact_exponential_distribution_density[1],
                                   'Exact exponential distribution', 'lab4/exponential_seq',
                                   'Exponential sequence (%s=%.3f)' % (r'$\lambda$', l),
                                   (0, range_bound))
