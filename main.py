import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Grid:
    def __init__(self, shape=(10, 10), boundary="fixed"):
        self.shape = shape
        self.boundary = boundary
        self.grid = self.generate_grid()
        self.KERNEL = np.asarray([[1, 1, 1], [1, 0, 1], [1, 1, 1]])  # The KERNEL to convolve cells

    def __repr__(self) -> str:
        return "\n" + str(self.grid).replace("[", " ").replace("]", " ") + "\n"

    def generate_grid(self) -> np.ndarray:
        return np.zeros(shape=self.shape, dtype=np.int8)

    def define_1(self, pos_x, pos_y) -> None:
        self.grid[pos_y][pos_x] = 1

    def define_0(self, pos_x, pos_y) -> None:
        self.grid[pos_y][pos_x] = 0

    @staticmethod
    def growth(U):
        return np.where(U == 3, 1, 0)

    def next_gen(self):  # Determine a cell's state by it's neighbour count
        self.grid = np.clip(
            self.grid + self.growth(signal.convolve2d(self.grid, self.KERNEL, mode='same', boundary='wrap')), 0, 1)


if __name__ == "__main__":
    frames = []
    grid = Grid(shape=(50, 50))
    grid.define_1(1, 0)
    grid.define_1(2, 1)
    grid.define_1(0, 2)
    grid.define_1(1, 2)
    grid.define_1(2, 2)
    for i in range(100):
        grid.next_gen()
        frames.append(grid.grid)
    # Set up the figure and subplot
    fig, ax = plt.subplots()
    print(frames)
    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


    def update_frame(num):
        ax.imshow(frames[num], cmap='gray')


    ani = animation.FuncAnimation(fig, update_frame, frames=range(len(frames)), repeat=True)
    ani.save('video.mp4', writer=writer)
