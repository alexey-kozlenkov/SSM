from matplotlib import pyplot as plot

__author__ = 'Alexey'


def plot_histogram(sequence, k, filename, title=None):
    plot.xkcd()
    plot.grid(True, linewidth=0.5, zorder=0)
    n, bins, patches = plot.hist(sequence, k, zorder=3)
    plot.ylim(0, max(n) * 1.25)
    plot.title(title if title else '')
    plot.savefig('../graphics/' + filename + '.png')
    plot.clf()