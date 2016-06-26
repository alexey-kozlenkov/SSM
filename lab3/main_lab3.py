import os

from util.generator.discrete_random_variable import bernoulli
from util.utils import get_average_and_dispersion

p = 0.5
n = 50000

bernoulli_sequence = bernoulli(n, p)

average, dispersion = get_average_and_dispersion(bernoulli_sequence)
print('Empiric average: %.3f vs theoretical average: %.3f' % (average, p))
print('Empiric dispersion: %.3f vs theoretical dispersion: %.3f' % (dispersion, p * (1 - p)))

out = open('input.txt', 'w')
out.writelines(list(map(str, bernoulli_sequence)))
out.close()

print('Running tests...')
os.system('python randomtests/testrandom.py -i input.txt -o output.txt -x -m')
print('Tests finished')
