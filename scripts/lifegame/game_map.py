# -*- coding: utf-8 -*-
#
# @author Norris183891

import random
import sys


class GameMap(object):
    
    MAX_MAP_SIZE = 100

    def __init__(self, rows, cols):
        """Inits GameMap with row and column count."""
        assert isinstance(rows, int)
        assert isinstance(cols, int)
        assert 0 < rows <= self.MAX_MAP_SIZE
        assert 0 < cols <= self.MAX_MAP_SIZE
        self.size = (rows, cols, )
        self.cells = [[0 for col in range(cols)] for row in range(rows)]

    @property
    def rows(self):
        return self.size[0]

    @property
    def cols(self):
        return self.size[1]

    def reset(self, possibility=0.5):
        """Reset the map with random data.

        Args:
            possibility: possibility of life cell
        """
        assert 0 <= possibility <= 1
        self.cells = [[(1 if random.random() <= possibility else 0) \
                       for col in range(self.cols)] for row in range(self.rows)]

    def set(self, row, col, val):
        """Set specific cell in the map."""
        assert isinstance(row, int)
        assert isinstance(col, int)
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols
        assert val in (0, 1)
        self.cells[row][col] = val

    def get_neighbor_count(self, row, col):
        """Get count of neighbors in specific cell.

        Args:
            row: row number
            col: column number

        Returns:
            Count of live neighbor cells
        """
        assert isinstance(row, int)
        assert isinstance(col, int)
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols
        neighbors = [self.cells[i if i < self.rows else 0][j if j < self.cols else 0] \
                     for i in range(row - 1, row + 2) for j in range(col - 1, col + 2)]
        return sum(neighbors) - self.cells[row][col]


    def get_neighbor_count_map(self):
        """Get count of neighbors of every cell in the map.

        Returns:
            A grid contains every cell's neighbor count.
        """
        return [[self.get_neighbor_count(row, col) for col in range(self.cols)] for row in range(self.rows)]

    def print_map(self, cell_maps=None, sep=' ', fd=sys.stdout):
        """Print the map to target file descriptor

        Args:
            cell_maps: mapping from cell value to a string that will be displayed.
            sep: separator between cells of the same row.
            fd: file descriptor, default standard output
        """
        if not cell_maps:
            cell_maps = ['0', '1']
        assert isinstance(cell_maps, list) or isinstance(cell_maps, dict)
        assert isinstance(sep, str)
        for row in self.cells:
            print(sep.join(map(lambda cell: cell_maps[cell], row)), file=fd)
