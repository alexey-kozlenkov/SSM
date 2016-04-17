__author__ = 'Alexey'


def get_average_and_dispersion(sequence):
    average = float(sum(sequence)) / len(sequence)
    dispersion = sum((x - average) ** 2 for x in sequence) / (len(sequence) - 1)
    return average, dispersion
