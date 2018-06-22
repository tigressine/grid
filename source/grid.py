class Grid:
    """Class that provides self-growing, coordinate-like list functionality.
   
    Items can be accessed by indexing (e.g. myGrid[y, x]) where y represents
    the 'height,' or number of rows down from the top to traverse, and x
    represents the 'width,' or number of items down the current row to traverse.
    """
    
    def __init__(self, height=0, width=0):
        """Initialize a new grid object."""
        self.grid = [[None for w in range(width)] for h in range(height)]
        self.height = height
        self.width = width
        self.items = 0

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
        
        # Check if the index is a tuple of indices.
        if isinstance(index, tuple):
            # Extend number of rows to accommodate given height index.
            heightDiff = (index[0] + 1) - self.height
            if heightDiff > 0:
                newRows = [[None for w in range(self.width)] for h in range(heightDiff)]
                self.grid.extend(newRows)
                self.height = index[0] + 1

            # Extend all rows to accommodate given width index.
            widthDiff = (index[1] + 1) - self.width
            if widthDiff > 0:
                for row in self.grid:
                    row.extend([None for w in range(widthDiff)])
                self.width = index[1] + 1

            # Change items count based on what is being inserted and where.
            if self.grid[index[0]][index[1]] is None:
                if item is not None:
                    self.items += 1
            else:
                if item is None:
                    self.items -= 1
           
            self.grid[index[0]][index[1]] = item
            
        # If index is solo, then item is for an entire row.
        elif isinstance(index, int):#needs to be reworked
            # Generate enough rows to handle the provided index.
            while index >= len(self.grid):
                self.grid.append([])

            # Make sure that the item inserted is in list form.
            if isinstance(item, list):
                self.grid[index] = item
            else:
                self.grid[index] = [item]
            self.items += 1 if item is not None else -1

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
        return self.items
