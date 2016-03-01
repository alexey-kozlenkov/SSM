__author__ = 'Alexey'
from math import sqrt, floor
from scipy.stats import chisquare


def method_of_moments_test(sequence, boundary):
    n = len(sequence)
    average = float(sum(sequence)) / n
    dispersion = float(sum((x - average) ** 2 for x in sequence)) / (n - 1)
    c_1 = sqrt(12 * n)
    c_2 = float(n - 1) / n * pow((0.0056 / n + 0.0028 / n ** 2 - 0.0083 / n ** 3), -0.5)
    return c_1 * abs(average - 0.5) < boundary, c_2 * abs(dispersion - 1. / 12) < boundary


def covariation_test(sequence, t, boundary):
    n = len(sequence)
    average = float(sum(sequence)) / n
    r = [0.] * (t - 1)
    r.append(1. / 12)
    r.reverse()
    r_estimation = [
        1. / (n - j - 1) * sum(sequence[0] *
                               sequence[1 + i] for i in range(n - j - 1)) -
        float(n) / (n - 1) * average ** 2 for j in range(t)]
    c = [1.] * (t - 1)
    c.append(sqrt(2))
    c.reverse()
    for i in range(t):
        if abs(r[i] - r_estimation[i]) < c[i] * boundary / (12 * sqrt(n - 1)):
            return False
    return True


def chi_square_test(sequence, k, boundary):
    pieces = {i: 0 for i in range(k)}
    for element in sequence:
        pieces[floor(element * k)] += 1
    chi2_test = chisquare(pieces.values())
    return chi2_test[1] >= 1 - boundary
