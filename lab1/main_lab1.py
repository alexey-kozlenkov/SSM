__author__ = 'Alexey'
from lab1.data import mcg_data, mmg_data
from util.generator.base_random_variable import multiplicative_congruential_generator, maclaren_marsaglia_generator
from histogram import plot_histogram
from tests import method_of_moments_test, covariation_test, chi_square_test

standard_distribution_quantile = 1.959964

mcg_result = multiplicative_congruential_generator(mcg_data.a0, mcg_data.M, mcg_data.beta, mcg_data.n)
print 'Multiplicative congruential generator: 1: %f, 100: %f, 900: %f, 1000: %f' % \
      (mcg_result[0], mcg_result[99], mcg_result[899], mcg_result[999])
plot_histogram(mcg_result, 20, 'mcg', title='Multiplicative congruential generator')
print 'Method of moments test: ', method_of_moments_test(mcg_result, standard_distribution_quantile)
print 'Covariation test: ', covariation_test(mcg_result, 30, standard_distribution_quantile)
print 'Chi-square test: ', chi_square_test(mcg_result, 40)

print

sequence_1 = multiplicative_congruential_generator(mcg_data.a0, mcg_data.M, mcg_data.beta, mcg_data.n + mmg_data.k)
sequence_2 = multiplicative_congruential_generator(mmg_data.a, mmg_data.M, max(mmg_data.c, mmg_data.M - mmg_data.c),
                                                   mmg_data.n)
mmg_result = maclaren_marsaglia_generator(sequence_1, sequence_2, mmg_data.k, 1000)
print 'MacLaren-Marsaglia generator: 1: %f, 100: %f, 900: %f, 1000: %f' % \
      (mmg_result[0], mmg_result[99], mmg_result[899], mmg_result[999])
plot_histogram(mmg_result, 20, 'maclaren-marsaglia', title='MacLaren-Marsaglia generator')
print 'Method of moments test: ', method_of_moments_test(mmg_result, standard_distribution_quantile)
print 'Covariation test: ', covariation_test(mmg_result, 30, standard_distribution_quantile)
print 'Chi-square test: ', chi_square_test(mmg_result, 40)
