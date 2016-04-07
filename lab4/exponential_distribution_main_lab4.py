from math import ceil
from lab4.function import build_exact_exponential_distribution_density
from util.plotter import plot_histogram_with_exact_function

__author__ = 'Alexey'
from util.generator.continious_random_variable import exponential

l = 0.25
n = 10000

print 'Exponential distribution: lambda=%f' % l
exponential_sequence = exponential(l, n)
average = sum(exponential_sequence) / n
dispersion = sum((x - average) ** 2 for x in exponential_sequence) / (n - 1)
print '\tEmpiric average: %f VS theoretical average: %f' % (average, 1. / l)
print '\tEmpiric dispersion: %f VS theoretical dispersion: %f' % (dispersion, 1. / l ** 2)


range_bound = ceil(max(map(abs, exponential_sequence)))
k = 40
exact_exponential_distribution_density = build_exact_exponential_distribution_density(l, n, range_bound)
plot_histogram_with_exact_function(exponential_sequence, k, exact_exponential_distribution_density[1],
                                   'Exact exponential distribution', 'lab4/exponential_seq',
                                   'Exponential sequence (%s=%.3f)' % (r'$\lambda$', l),
                                   (0, range_bound))
