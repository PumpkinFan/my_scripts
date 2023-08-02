import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from functools import partial

N_ITER = 25
X_RES = 100
Y_RES = 100

def mandle_func(z: complex, c: complex) -> complex:
    return z ** 2 + c

def make_complex_grid(x_start, x_stop, x_num, y_start, y_stop, y_num):
    """x is the real component of the complex number and y is the imaginary component"""
    x_grid = np.linspace(x_start, x_stop, x_num)
    y_grid = np.linspace(y_start, y_stop, y_num)
    xx, yy = np.meshgrid(x_grid, y_grid)
    return xx + yy*1j


def determine_convergence(c_grid):
    """return array of the same shape with 0 indicating divergence and 1 indicating convergence"""
    new_grid = np.zeros(c_grid.shape)
    for _ in range(N_ITER):
        new_grid = mandle_func(new_grid, c_grid)
    magnitudes = np.abs(new_grid)
    return np.where(np.isnan(magnitudes) | (magnitudes > 2), 0, 1)



def main():
    complex_grid = make_complex_grid(-2.5, 0.5, X_RES+1, -1.5, 1.5, Y_RES+1)
    binary_img = determine_convergence(complex_grid)

    # event handler function for zooming in on plot
    def on_zoom(event):
        # i, j are indices of x, y in complex_grid
        i_start, i_stop = map(int, ax.get_xlim())
        j_stop, j_start = map(int, ax.get_ylim())

        print(i_start, i_stop)
        
        new_start = complex_grid[j_start, i_start]
        new_x_start, new_y_start = np.real(new_start), np.imag(new_start)
        new_stop = complex_grid[j_stop, i_stop]
        new_x_stop, new_y_stop = np.real(new_stop), np.imag(new_stop)

        print(new_start, new_stop)

        new_complex_grid = make_complex_grid(new_x_start, new_x_stop, X_RES+1, new_y_start, new_y_stop, Y_RES+1)
        new_binary_img = determine_convergence(new_complex_grid)
        im.set_array(new_binary_img)
        plt.draw()

        ax.set_xlim(i_start, i_stop)
        ax.set_ylim(j_stop, j_start)
    

    fig, ax = plt.subplots()
    # rs = RectangleSelector(ax, onselect, drawtype="box", useblit=True, button=[1], minspanx=5, minspany=5, spancoords='pixels')

    im = ax.imshow(binary_img)
    cid = fig.canvas.mpl_connect("axes_enter_event", on_zoom)  # connect zoom event to our on_zoom function

    # ax.set_xlabel("Real")
    # ax.set_ylabel("Imaginary")
    # x_step = X_RES // 10
    # y_step = Y_RES // 10
    # ax.set_xticks(range(len(x_grid))[::x_step], np.round(x_grid[::x_step], 1))
    # ax.set_yticks(range(len(y_grid))[::y_step], np.round(y_grid[::y_step], 1))
    
    plt.show()


if __name__ == "__main__":
    main()