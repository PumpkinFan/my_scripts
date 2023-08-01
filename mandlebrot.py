import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

N_ITER = 25
X_RES = 1000
Y_RES = 1000

def mandle_func(z: complex, c: complex) -> complex:
    return z ** 2 + c

def main():
    x_grid = np.linspace(-2.5, 0.5, X_RES+1)
    y_grid = np.linspace(-1.5, 1.5, Y_RES+1)
    xx, yy = np.meshgrid(x_grid, y_grid)
    complex_grid = xx + yy*1j
    
    new_grid = np.zeros(complex_grid.shape)

    for _ in range(N_ITER):
        new_grid = mandle_func(new_grid, complex_grid)

    magnitudes = np.abs(new_grid)
    binary_img = np.where(np.isnan(magnitudes) | (magnitudes > 2), 0, 1)

    plt.imshow(binary_img)
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    x_step = X_RES // 10
    y_step = Y_RES // 10
    plt.xticks(range(len(x_grid))[::x_step], np.round(x_grid[::x_step], 1))
    plt.yticks(range(len(y_grid))[::y_step], np.round(y_grid[::y_step], 1))
    plt.show()
    return

if __name__ == "__main__":
    main()