class Grid:
    """Class that provides self-growing, coordinate-like list functionality.
   
    Items can be accessed by indexing (e.g. myGrid[y, x]) where y represents
    the 'height,' or number of rows down from the top to traverse, and x
    represents the 'width,' or number of items down the current row to traverse.
    """
    
    def __init__(self):
        """Initialize a new grid object."""
        self.grid = [[]]

    def __getitem__(self, index):
        """Retrieve item from grid.
        
        Throws IndexError if the provided index or indices are out of bounds.
        """
        if isinstance(index, tuple):
            return self.grid[index[0]][index[1]]
        else:
            return self.grid[index]

    def __setitem__(self, index, item):
        """Set item or row in grid based on provided index."""
        
        # Check if the index is actually a tuple of indices.
        if isinstance(index, tuple):
            # Generate enough rows to handle the provided index.
            while index[0] >= len(self.grid):
                self.grid.append([])

            # Generate enough items in the requested row to support
            # the provided index.
            while index[1] >= len(self.grid[index[0]]):
                self.grid[index[0]].append(None)

            self.grid[index[0]][index[1]] = item

        # If index is solo, then item is for an entire row.
        elif isinstance(index, int):
            # Generate enough rows to handle the provided index.
            while index >= len(self.grid):
                self.grid.append([])

            # Make sure that the item inserted is in list form.
            if isinstance(item, list):
                self.grid[index] = item
            else:
                self.grid[index] = [item]

    def __str__(self):
        """Return a printable string representation of the grid."""
        rows = []
        for row in self.grid:
            # Add all items of row into a single string with join(),
            # then add that row to the rows list.
            rows.append("[{}]".format(", ".join(str(item) for item in row)))

        # Return all of the rows in the rows list as a single string.
        return "\n".join(rows)

    def __len__(self):
        """Return count of all objects in grid."""
        return sum(len(row) for row in self.grid)


grid = Grid()

grid[0] = [x for x in range(10)]
grid[1] = [x for x in reversed(range(0, 10))]
grid[1, 3] = 9001
grid[2] = "hello"
grid[2, 1] = "world"
grid[4, 4] = "generated some garbage"
grid[5] = []
grid[6] = []
grid[-1] = "spooky"
grid[-1, 6] = "like wut"

print("Grid:")
print(grid)
print("\nSelected lines and items:")
print(grid[1, 3])
print(grid[-1])
print(grid[4])
print(grid[5])
print(len(grid))
