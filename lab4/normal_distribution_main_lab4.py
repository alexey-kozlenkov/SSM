from lab4.function import build_exact_normal_distribution_density
from util.plotter import plot_histogram, plot_histogram_with_exact_function

__author__ = 'Alexey'
from util.generator.continious_random_variable import normal

m = -2
s2 = 1
n = 10000
N = 42

normal_distribution = normal(m, s2, n, N)
print 'Normal distribution(%f, %f):' % (m, s2)
average = sum(normal_distribution) / n
dispersion = sum((x - average) ** 2 for x in normal_distribution) / (n - 1)
print '\tActual average: ' + str(average)
print '\tActual dispersion: ' + str(dispersion)

k = 25
range_bound = max(map(abs, normal_distribution))
exact_normal_distribution_density = build_exact_normal_distribution_density(m, s2, n)
plot_histogram_with_exact_function(normal_distribution, k, exact_normal_distribution_density[1],
                                   'Exact normal distribution', 'lab4/normal_seq', 'Normal distribution(%.3f, %.3f)' % (m, s2),
                                   (-range_bound, range_bound))

