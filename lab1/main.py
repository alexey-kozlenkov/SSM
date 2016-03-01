__author__ = 'Alexey'
from lab1.data import mcg_data, mmg_data
from generator import multiplicative_congruential_generator, maclaren_marsaglia_generator
from histogram import plot_histogram

mcg_result = multiplicative_congruential_generator(mcg_data.a0, mcg_data.M, mcg_data.beta, mcg_data.n)
print 'Multiplicative congruential generator: 1: %f, 100: %f, 900: %f, 1000: %f.' % \
      (mcg_result[0], mcg_result[99], mcg_result[899], mcg_result[999])
plot_histogram(mcg_result, 20, 'mcg', title='Multiplicative congruential generator')


sequence_1 = multiplicative_congruential_generator(mcg_data.a0, mcg_data.M, mcg_data.beta, mcg_data.n + mmg_data.k)
sequence_2 = multiplicative_congruential_generator(mmg_data.a, mmg_data.M, max(mmg_data.c, mmg_data.M - mmg_data.c),
                                                   mmg_data.n)
result_sequence = maclaren_marsaglia_generator(sequence_1, sequence_2, mmg_data.k, 1000)
print 'MacLaren-Marsaglia generator: 1: %f, 100: %f, 900: %f, 1000: %f.' % \
      (result_sequence[0], result_sequence[99], result_sequence[899], result_sequence[999])
plot_histogram(result_sequence, 20, 'maclaren-marsaglia', title='MacLaren-Marsaglia generator')
