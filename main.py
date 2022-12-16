import plotly as pl
import numpy as np
from scipy import signal

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
        return 0 + (U == 3) - ((U < 2) | (U > 3))  # Returning the growth of a specific cell U

    def next_gen(self):  # Determine a cell's state by it's neighbour count
        self.grid = np.clip(
            self.grid + self.growth(signal.convolve2d(self.grid, self.KERNEL, mode='same', boundary='wrap')), 0, 1)


# animate this array by calling the grid.next_gen() function
grid = Grid(shape=(100, 100), boundary="wrap")
# create a glider
grid.define_1(1, 0)
grid.define_1(2, 1)
grid.define_1(0, 2)
grid.define_1(1, 2)
grid.define_1(2, 2)



# animate this array by calling the grid.next_gen() function usig plotly. save the animation as a gif


def animate_grid(grid, frames=100, interval=100, filename="animation.gif"):
    fig = pl.make_subplots(rows=1, cols=1)
    fig.update_layout(
        title_text="Conway's Game of Life",
        xaxis=dict(range=[0, grid.shape[0]], autorange=False, zeroline=False),
        yaxis=dict(range=[0, grid.shape[1]], autorange=False, zeroline=False),
        updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])],
    )

    frames = [pl.graph_objects.Frame(data=pl.graph_objects.Heatmap(z=grid.grid))]

    for i in range(frames):
        grid.next_gen()
        frames.append(pl.graph_objects.Frame(data=pl.graph_objects.Heatmap(z=grid.grid)))

    fig.update(frames=frames)
    fig.write_image(filename, engine="kaleido", format="gif", mode="loop", duration=interval)
    fig.show()


animate_grid(grid, frames=100, interval=100, filename="animation.gif")