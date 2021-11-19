from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

matplotlib.use('TkAgg')


def get_fig(x_axis, y_axis):
    """
    Generates a matplotlib figure

    :param x_axis: Values on the x axis
    :type x_axis: string
    :param y_axis: Values on the y axis
    :type y_axis: string
    """
    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot().plot(x_axis, y_axis)
    return fig


def draw_figure(canvas, figure):
    """
        Draws a figure on a canvas

        :param canvas: Canvas to draw figure on
        :type canvas: Union[() -> Canvas, () -> Canvas]
        :param figure: Figure to draw
        :type figure: string
    """
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


