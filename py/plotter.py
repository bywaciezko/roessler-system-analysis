import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


def plot(
    file_path,
    path_x,
    path_y,
    x_label,
    y_label,
    alpha_,
    DPI,
    major_ticker,
    minor_ticker,
    format,
    marker_format,
    marker_size=None,
    custom_draw=None,
    xlim=None,
    ylim=None,
):
    x = pd.read_csv(path_x, header=None)
    y = pd.read_csv(path_y, header=None)

    plt.figure(dpi=DPI)

    if marker_size is not None:
        plt.plot(
            x, y, marker_format, markersize=marker_size, alpha=alpha_, color="black"
        )
    else:
        plt.plot(x, y, marker_format, alpha=alpha_, color="black")

    ax = plt.gca()

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    for spine in ax.spines.values():
        spine.set_linewidth(0.3)
        spine.set_color("black")

    ax.tick_params(width=0.3, color="black", labelsize=6)
    ax.tick_params(which="minor", width=0.3, color="black", labelsize=4)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(major_ticker))
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter(format))

    ax.xaxis.set_minor_locator(ticker.MultipleLocator(minor_ticker))
    ax.xaxis.set_minor_formatter(ticker.NullFormatter())

    if custom_draw:
        custom_draw(ax)
    plt.savefig(file_path, bbox_inches="tight")
