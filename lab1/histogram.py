__author__ = 'Alexey'
from matplotlib import pyplot as plot


def plot_histogram(sequence, k, filename, title=None):
    plot.xkcd()
    plot.grid(True, linewidth=0.5, zorder=0)
    plot.ylim(0, len(sequence) * 1.5 / k)
    plot.hist(sequence, k, zorder=3)
    plot.title(title if title else '')
    plot.savefig('graphics/' + filename + '.png')
    plot.clf()
