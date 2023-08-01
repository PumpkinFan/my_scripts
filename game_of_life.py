"""inspired by: https://www.youtube.com/watch?v=pMslgySQ8nc"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def life_init(h, w=None):
    if w is None:
        return np.random.randint(0, 2, size=(h, h*2))
    else:
        return np.random.randint(0, 2, size=(h, w))

def life_iter(game_arr):
    mid_row = np.stack(
        (np.roll(game_arr, -1, axis=1), game_arr, np.roll(game_arr, 1, axis=1)), axis=0
    )
    whole_arr = np.stack(
        (np.roll(mid_row, -1, axis=1), mid_row, np.roll(mid_row, 1, axis=1)), axis=0
    )
    neighbor_arr = np.sum(np.sum(whole_arr, axis=1), axis=0)
    return np.where(((neighbor_arr == 4) & game_arr.astype(bool)) | (neighbor_arr == 3), 1, 0)


def main(n_iters):
    game_arr = life_init(50)

    # initialize a glider (https://conwaylife.com/wiki/Glider)
    # game_arr = np.zeros((10,10))
    # game_arr[1, 3] = 1
    # game_arr[2, 3] = 1
    # game_arr[3, 3] = 1
    # game_arr[3, 2] = 1
    # game_arr[2, 1] = 1

    fig, ax = plt.subplots()
    frames = []
    for _ in range(n_iters):
        im = ax.imshow(game_arr, cmap="binary")
        game_arr = life_iter(game_arr)
        frames.append([im])

    _ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat_delay=1000)
    plt.show()

main(1000)