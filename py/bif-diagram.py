from matplotlib.pyplot import ylim
import plotter
import pandas as pd

# all
# A = pd.read_csv("../output/boundries.csv", header=None)
# file_path = "../images/bif-boundries.png"
# path_x = "../output/bif-a.csv"
# path_y = "../output/bif-x.csv"

# first
lower_bound = 4.380026185035703
upper_bound = 4.3956232464929856
file_path = "../images/fpw-bif.png"
path_x = "../output/fpw-bif-a.csv"
path_y = "../output/fpw-bif-x.csv"

# second
# lower_bound = 4.694104184150694
# upper_bound = 4.7207655310621242
# file_path = "../images/spw-bif.png"
# path_x = "../output/spw-bif-a.csv"
# path_y = "../output/spw-bif-x.csv"

# third
# lower_bound = 5.185404746055601
# upper_bound = 5.497374749498998
# file_path = "../images/tpw-bif.png"
# path_x = "../output/tpw-bif-a.csv"
# path_y = "../output/tpw-bif-x.csv"


def draw_extras(ax):
    # highlight_bounds(ax, A[0])
    draw_boundries(ax)


def draw_boundries(ax):
    ymin, ymax = ax.get_ylim()
    text_y = ymax + 0.02 * (ymax - ymin)  # 2% nad górną granicą

    ax.axvline(lower_bound, color="blue", linewidth=0.2, linestyle="--")
    ax.text(
        lower_bound,
        text_y,
        f"{lower_bound:.4f}",
        rotation=90,
        verticalalignment="bottom",
        horizontalalignment="center",
        fontsize=4,
        color="blue",
    )

    ax.axvline(upper_bound, color="green", linewidth=0.2, linestyle="--")
    ax.text(
        upper_bound,
        text_y,
        f"{upper_bound:.4f}",
        rotation=90,
        verticalalignment="bottom",
        horizontalalignment="center",
        fontsize=4,
        color="green",
    )


# def highlight_bounds(ax, bounds, color="red", alpha=0.1):
#     ymin, ymax = ax.get_ylim()
#     text_y = ymax + 0.02 * (ymax - ymin)
#
#     labels = [r"I", r"II", r"III"]
#     for i in range(0, len(bounds), 2):
#         lower = bounds[i]
#         upper = bounds[i + 1]
#
#         ax.axvspan(lower, upper, color=color, alpha=alpha, ec=None)
#
#         mid = (lower + upper) / 2
#         ax.text(
#             mid,
#             text_y,
#             labels[i // 2],
#             ha="center",
#             va="top",
#             fontsize=6,
#             color=color,
#         )


x_label = "c"
y_label = "y"
alpha_ = 0.6
DPI = 600
major_ticker = 0.005
minor_ticker = 0.0005
format = "%.3f"
markerformat = ","

plotter.plot(
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
    markerformat,
    custom_draw=draw_extras,
)
