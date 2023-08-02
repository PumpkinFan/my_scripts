import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector, Button

N_ITER = 25
X_RES = 1000
Y_RES = 1000

def mandle_func(z: complex, c: complex) -> complex:
    return z ** 2 + c

def make_complex_grid(x_start, x_stop, x_num, y_start, y_stop, y_num) -> np.ndarray:
    """create a 2D grid of complex numbers with uniform spacing in both directions"""
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
    initial_complex_grid = make_complex_grid(-2.5, 0.5, X_RES+1, -1.5, 1.5, Y_RES+1)
    initial_binary_img = determine_convergence(initial_complex_grid)
    complex_grid = initial_complex_grid.copy()
    binary_img = initial_binary_img.copy()

    # event handler function for "zooming" in on plot
    # instead of just zooming this actually computes the mandlebrot set in the newly selected range
    # the plot is then changed to show the set in this new range
    def onselect(eclick, erelease):
        # i, j are indices of x, y in complex_grid
        i_start, j_start = map(int, (eclick.xdata, eclick.ydata))
        i_stop, j_stop = map(int, (erelease.xdata, erelease.ydata))

        print(eclick.xdata, eclick.ydata, erelease.xdata, erelease.ydata)
        
        new_start = complex_grid[j_start, i_start]
        new_x_start, new_y_start = np.real(new_start), np.imag(new_start)
        new_stop = complex_grid[j_stop, i_stop]
        new_x_stop, new_y_stop = np.real(new_stop), np.imag(new_stop)

        new_complex_grid = make_complex_grid(new_x_start, new_x_stop, X_RES+1, new_y_start, new_y_stop, Y_RES+1)
        new_binary_img = determine_convergence(new_complex_grid)
        im.set_array(new_binary_img)
        plt.draw()

        complex_grid[:, :] = new_complex_grid.copy()

    # event handler to reset plot
    def reset_button_clicked(event):
        im.set_array(initial_binary_img)
        plt.draw()
        complex_grid[:, :] = initial_complex_grid.copy()

    fig, ax = plt.subplots()
    rs = RectangleSelector(ax, onselect, useblit=True, button=[1], minspanx=5, minspany=5, spancoords='pixels')
    reset_button = Button(plt.axes([0.7, 0.01, 0.2, 0.05]), "Reset")
    reset_button.on_clicked(reset_button_clicked)

    im = ax.imshow(binary_img)

    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    x_grid = np.real(complex_grid)[0, :]
    y_grid = np.imag(complex_grid)[:, 0]
    x_step = X_RES // 10
    y_step = Y_RES // 10
    ax.set_xticks(range(len(x_grid))[::x_step], np.round(x_grid[::x_step], 1))
    ax.set_yticks(range(len(y_grid))[::y_step], np.round(y_grid[::y_step], 1))
    
    plt.show()


if __name__ == "__main__":
    main()