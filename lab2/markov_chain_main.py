from lab1.data import mcg_data
from lab2.function import build_chain
from util.generator.base_random_variable import multiplicative_congruential_generator

n = 100
s = [0, 1, 2]
t = 1000
p_0 = [(1, s[0]), (0, s[1]), (0, s[2])]
p = [[(0.1, s[0]), (0.2, s[1]), (0.7, s[2])],
     [(0.3, s[0]), (0.4, s[1]), (0.3, s[2])],
     [(0.6, s[0]), (0.2, s[1]), (0.2, s[2])]]

base_sequence = multiplicative_congruential_generator(mcg_data.a0, mcg_data.M, mcg_data.beta, t)
chain = build_chain(p, p_0, base_sequence)
print('Percentage: {:d}: {:.3f}, {:d}: {:.3f}, {:d}: {:.3f}'.format(s[0], float(chain.count(s[0])) / t, s[1], float(chain.count(s[1])) / t, s[2], float(chain.count(s[2])) / t))
