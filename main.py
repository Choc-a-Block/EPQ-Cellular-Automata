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
        return np.where(U == 3, 1, 0)

    def next_gen(self):  # Determine a cell's state by it's neighbour count
        self.grid = np.clip(
            self.grid + self.growth(signal.convolve2d(self.grid, self.KERNEL, mode='same', boundary='wrap')), 0, 1)


# a function to animate the grid. show the grid moving in a plotly graph
def animate_grid(grid, steps=100):
    # create a list of frames
    frames = []
    for i in range(steps):
        frames.append(pl.graph_objects.Frame(data=pl.graph_objects.Heatmap(z=grid.grid)))
        grid.next_gen()
    # create the figure
    fig = pl.graph_objects.Figure(
        data=pl.graph_objects.Heatmap(z=grid.grid),
        layout=pl.graph_objects.Layout(
            xaxis=dict(range=[0, grid.shape[1]], autorange=False),
            yaxis=dict(range=[0, grid.shape[0]], autorange=False),
            title_text="Conway's Game of Life",
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label="Animate",
                              method="animate",
                              args=[None])])]),
        frames=frames)
    fig.show()


if __name__ == '__main__':
    # animate this array by calling the grid.next_gen() function
    grid = Grid(shape=(10, 10), boundary="wrap")
    # define the initial state of the grid
    grid.define_1(1, 1)
    grid.define_1(1, 2)
    grid.define_1(2, 1)
    grid.define_1(2, 2)
    grid.define_1(3, 3)
    grid.define_1(3, 4)
    grid.define_1(4, 3)
    grid.define_1(4, 4)
    grid.define_1(5, 5)
    grid.define_1(5, 6)

    animate_grid(grid, steps=100)
