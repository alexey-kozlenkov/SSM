from util.generator.continious_random_variable import normal_standard_by_box_muller
from util.plotter import plot_two_histograms
from util.utils import get_average_and_dispersion

__author__ = 'Alexey'

n_start = 10000
first_seq, second_seq = normal_standard_by_box_muller(n_start)
n = len(first_seq)
print('Box-muller transformation for generating normal standard sequences ' \
      'returned sequences with %f filling.' % (float(n) / n_start))

print('First sequence:')
average, dispersion = get_average_and_dispersion(first_seq)
print('\tEmpiric average: %f' % average)
print('\tEmpiric dispersion: %f' % dispersion)

print('Second sequence:')
average, dispersion = get_average_and_dispersion(second_seq)
print('\tEmpiric average: %f' % average)
print('\tEmpiric dispersion: %f' % dispersion)

k = 25
plot_two_histograms(first_seq, second_seq, k, r'$z_0$', r'$z_1$', 'lab4/box_muller',
                    'N(0, 1) by Box-Muller transformation')
