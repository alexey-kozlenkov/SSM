from math import ceil

from lab4.function import build_exact_normal_distribution_density
from util.generator.continious_random_variable import normal
from util.plotter import plot_histogram_with_exact_function

m = -2
s2 = 1
n = 10000
N = 42

print('Normal distribution(%f, %f):' % (m, s2))
normal_distribution_sequence = normal(m, s2, n, N)
average = sum(normal_distribution_sequence) / n
dispersion = sum((x - average) ** 2 for x in normal_distribution_sequence) / (n - 1)
print('\tEmpiric average: ' + str(average))
print('\tEmpiric dispersion: ' + str(dispersion))

k = 40
range_bound = ceil(max(list(map(abs, normal_distribution_sequence))))
exact_normal_distribution_density = build_exact_normal_distribution_density(m, s2, n, -range_bound, range_bound)
plot_histogram_with_exact_function(normal_distribution_sequence, k, exact_normal_distribution_density[1],
                                   'Exact normal distribution', 'lab4/normal_seq',
                                   'Normal distribution (%s=%.3f, %s=%.3f)' % (r'$\mu$', m, r'$\sigma^2$', s2),
                                   (-range_bound, range_bound))
