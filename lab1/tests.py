__author__ = 'Alexey'
from math import sqrt, floor

from scipy.stats import chi2


def method_of_moments_test(sequence, quantile):
    n = len(sequence)
    average = float(sum(sequence)) / n
    dispersion = float(sum((x - average) ** 2 for x in sequence)) / (n - 1)
    c_1 = sqrt(12 * n)
    c_2 = float(n - 1) / n * pow((0.0056 / n + 0.0028 / n ** 2 - 0.0083 / n ** 3), -0.5)
    return c_1 * abs(average - 0.5) < quantile, c_2 * abs(dispersion - 1. / 12) < quantile


def covariation_test(sequence, t, quantile):
    n = len(sequence)
    average = sum(sequence) / n
    r = [0.] * (t - 1)
    r.append(1. / 12)
    r.reverse()
    r_estimation = [
        1. / (n - j - 1) * sum(sequence[i] * sequence[i + j] for i in range(n - j - 1)) -
        (float(n) * average ** 2) / (n - 1) for j in range(t)]
    c = [1.] * (t - 1)
    c.append(sqrt(2))
    c.reverse()
    for i in range(t):
        if abs(r[i] - r_estimation[i]) < c[i] * quantile / (12. * sqrt(n - 1)):
            return False, i
    return True


def chi_square_test(sequence, k):
    frequencies = {i: 0 for i in range(k)}
    for element in sequence:
        frequencies[floor(element * k)] += 1
    expected_frequency = float(len(sequence)) / k
    chi_square = sum((frequencies[i] - expected_frequency) ** 2 / expected_frequency for i in range(k))
    return chi_square, chi2.cdf(chi_square, k-1)
