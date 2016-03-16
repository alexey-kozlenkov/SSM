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


def plot_histogram_with_exact_function(sequence, k, exact_y, exact_title, filename, title=None):
    plot.xkcd()
    plot.grid(True, linewidth=0.5, zorder=0)
    n, bins, patches = plot.hist(sequence, k, zorder=3, label='Histogram')
    plot.ylim(0, max(n) * 1.25)

    bin_centers = [0.5 * (bins[i] + bins[i + 1]) for i in range(k)]
    plot.plot(bin_centers, map(lambda y: y * len(sequence), exact_y[::len(exact_y) / k]), color='red',
              label=exact_title, zorder=3)

    plot.title(title if title else '')
    plot.legend()
    plot.savefig('../graphics/' + filename + '.png')
    plot.clf()
