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


def plot_histogram_with_exact_function(sequence, k, exact_y, exact_label, filename, title=None, range_p=None):
    plot.xkcd()
    plot.grid(True, linewidth=0.5, zorder=0)
    n, bins, patches = plot.hist(sequence, k, range=range_p, normed=True, zorder=3, label='Histogram')

    bin_centers = [0.5 * (bins[i] + bins[i + 1]) for i in range(k)]
    plot.plot(bin_centers, exact_y[::len(exact_y) / k][:k], color='red', label=exact_label, zorder=3)

    plot.xticks()
    plot.title(title if title else '')
    leg = plot.legend(loc=9, bbox_to_anchor=(0.5, -0.05), ncol=2)
    plot.savefig('../graphics/' + filename + '.png', bbox_inches='tight', additional_artists=(leg,))
    plot.clf()


def plot_two_functions(x1, y1, label1, x2, y2, label2, filename, title=None):
    plot.xkcd()
    plot.grid(True, linewidth=0.5, zorder=0)

    plot.plot(x1, y1, color='blue', label=label1)
    plot.plot(x2, y2, color='red', label=label2)

    plot.title(title if title else '')
    leg = plot.legend(loc=9, bbox_to_anchor=(0.5, -0.05), ncol=2)
    plot.savefig('../graphics/' + filename + '.png', bbox_inches='tight', additional_artists=(leg,))
    plot.clf()


def plot_two_histograms(sequence1, sequence2, k, label1, label2, filename, title=None, range_p=None):
    plot.xkcd()
    plot.hist(sequence1, k, label=label1, range=range_p, normed=True, color='blue', alpha=0.5)
    plot.hist(sequence2, k, label=label2, range=range_p, normed=True, color='green', alpha=0.5)
    plot.title(title if title else '')
    plot.legend(loc='upper right')
    plot.savefig('../graphics/' + filename + '.png')
    plot.clf()
