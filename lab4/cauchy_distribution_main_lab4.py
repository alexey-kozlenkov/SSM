from math import ceil
from lab4.function import build_exact_cauchy_distribution_density
from util.generator.continious_random_variable import cauchy
from util.plotter import plot_histogram_with_exact_function, plot_histogram

__author__ = 'Alexey'

m = 1.
c = 2.
n = 10000

print 'Cauchy distribution:'
cauchy_sequence = cauchy(m, c, n)
print 'Average and dispersion are not defined.'
print 'Empiric median:  %f VS theoretical median: %f' % (sorted(cauchy_sequence)[n/2], m)

# range_bound = ceil(max(map(abs, cauchy_sequence)))
range_bound = 20
k = 41
exact_cauchy_distribution_density = build_exact_cauchy_distribution_density(m, c, n, -range_bound, range_bound)
plot_histogram_with_exact_function(cauchy_sequence, k, exact_cauchy_distribution_density[1],
                                   'Exact Cauchy distribution', 'lab4/cauchy_seq',
                                   'Cauchy sequence (m=%.3f, c=%.3f)' % (m, c),
                                   (-range_bound, range_bound))

