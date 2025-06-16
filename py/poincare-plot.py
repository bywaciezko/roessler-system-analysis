import plotter

file_path = "../obrazki/poincare.png"
path_x = "../output/y_output.csv"
path_y = "../output/py_output.csv"
x_label = "y"
y_label = "P(y)"
alpha_ = 1
DPI = 300
major_ticker = 1
minor_ticker = 0.5
format = "%.1f"
markerformat = "o"
markersize = 2

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
    markersize,
)
