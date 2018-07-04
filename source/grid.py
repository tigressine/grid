class Grid:
    """A self-growing 2D array class.

    Grids are actually stored as an array of dictionaries. This means that
    very sparse 2D arrays (e.g. arrays with lots of None values) can be stored
    efficiently using this class, while maintaining an expected runtime of O(1)
    for insertions and lookups.
    """

    def __init__(self):
        """Initialize the grid."""
        self.items = 0
        self.width = 0
        self.height = 0
        self.grid = [{}]

    def __getitem__(self, indices):
        """Return item at given indices, if it exists."""
        indices = self.__sanitize_indices(indices)

        # If there's only a single index, then the entire row is desired.
        if len(indices) == 1:
            return self.__make_list(self.grid[indices[0]])

        # Else a specific item is desired. Return that item if it exists.
        return self.grid[indices[0]][indices[1]]

    def __setitem__(self, indices, item):
        """Set an item or list of items at the given indices in the grid."""
        indices = self.__sanitize_indices(indices)

        # Add rows until the grid can accommodate the indices's height.
        while indices[0] >= self.height:
            self.grid.append({})
            self.height += 1

        if len(indices) == 1:
            self.__set_row(indices[0], item)
        else:
            self.__set_item(indices, item)

    def __str__(self):
        """Return a simple string representation of the grid."""
        string = ""

        for row in range(self.height):
            for column in range(self.width):
                if column not in self.grid[row]:
                    string += '{:<15s}'.format("None")
                else:
                    string += '{:<15s}'.format(str(self.grid[row][column]))
            string += '\n' if row < self.height - 1 else ''

        return string

    def __len__(self):
        """Return the item count of the grid."""
        return self.items

    def capacity(self):
        """Return the area of the grid.

        The term "capacity" is misleading here since the grid will grow
        to whatever size it needs to be.
        """
        return self.width * self.height

    def __set_item(self, indices, item):
        """Set an item in the grid."""
        if indices[1] >= self.width:
            self.width = indices[1] + 1

        # Adjust the items count appropriately based on the change being made.
        if item is None and indices[1] in self.grid[indices[0]]:
            self.items -= 1
        elif item is not None and indices[1] not in self.grid[indices[0]]:
            self.items += 1

        self.grid[indices[0]][indices[1]] = item

    def __set_row(self, index, row):
        """Set an entire row in the grid."""
        self.items -= len(self.grid[index])

        # Reset the row.
        self.grid[index] = {}

        # If the row is not a tuple or a list, make it an iterable list.
        if not isinstance(row, tuple) and not isinstance(row, list):
            row = [row]

        # Add each value of the item list to the grid at the correct indices.
        for key, value in enumerate(row):
            if value is not None:
                self.grid[index][key] = value

                # If the inserting indices forces the row to be wider, change
                # the width of the whole grid.
                if key >= self.width:
                    self.width = key + 1

        # Add the count of all items in the new row to the total item count.
        self.items += len(self.grid[index])

    def __sanitize_indices(self, indices):
        """Sanitize the provided indices.

        The indices can be a tuple of integers, or a single integer. This
        function always returns a list, either with one or two indices.
        Further, the indices will always be positive.
        """

        # Confirm the indices are of the proper type and put them into a list.
        if isinstance(indices, tuple):
            if isinstance(indices[0], int) and isinstance(indices[1], int):
                indices = list(indices)
                # If the height index is negative, convert to the
                # positive analog.
                indices[1] += self.width if indices[1] < 0 else 0
            else:
                raise TypeError('Grid can only be indexed by integers.')

            # If the width index was so negative as to remain negative after
            # adding the width of the whole grid, then throw an error.
            if indices[1] < 0:
                raise IndexError('Negative index is out of bounds.')

        elif isinstance(indices, int):
            indices = [indices]

        else:
            raise TypeError('Grid can only be indexed by integers.')

        # If the height index is negative, convert to the positive analog.
        indices[0] += self.height if indices[0] < 0 else 0

        # If the height index was so negative as to remain negative after
        # adding the height of the whole grid, then throw an error.
        if indices[0] < 0:
            raise IndexError("Negative index is out of bounds")

        return indices

    def __make_list(self, grid_row):
        """Create a list from a dictionary of indexed items."""
        row = [None for each in range(self.width)]

        for item in grid_row.keys():
            row[item] = grid_row[item]

        return row
