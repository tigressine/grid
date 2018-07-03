class Grid:
    """A self-growing 2D array class.

    Grids are actually stored as an array of dictionaries. This means that
    very sparse 2D arrays (e.g. arrays with lots of None values) can be stored 
    efficiently using this class, while maintaining an expected runtime of O(1)
    for insertions and lookups.
    """

    def __init__(self):
        """Initialize the grid."""
        self.grid = [{}]
        self.height = 0
        self.width = 0
        self.items = 0

    def __getitem__(self, index):
        """Return item at index, if it exists."""
        index = self.sanitizeIndex(index)

        # Height bounds check.
        if index[0] < 0 or index[0] >= self.height:
            return None

        # If the length of index is 1, then the entire row is desired.
        if len(index) == 1:
            return self.makeList(self.grid[index[0]])

        # Else a specific item is desired. Return that item if it exists.
        elif len(index) == 2 and index[1] in self.grid[index[0]]:
            return self.grid[index[0]][index[1]]

        # Else something went wrong or the index didn't exist.
        else:
            return None

    def __setitem__(self, index, item):
        """Set an item or list of items at index in the grid."""
        index = self.sanitizeIndex(index)
      
        # Height bounds check.
        if index[0] < 0:
            return

        # Add rows until the grid can accommodate the index's height.
        while index[0] >= self.height:
            self.grid.append({})
            self.height += 1
      
        # If length of index is 1, then entire row is being set.
        if len(index) == 1:
            # Subtract the count of all the items in the row that currently
            # exists at index[0].
            self.items -= len(self.grid[index[0]])

            # Reset the row.
            self.grid[index[0]] = {}

            # Add each value of the item list to the grid at the correct index.
            for i, value in enumerate(item):
                if value is not None:
                    self.grid[index[0]][i] = value
                    
                    # If the inserting index forces the row to be wider, change
                    # the width of the whole grid.
                    if i >= self.width:
                        self.width = i + 1

            # Add the count of all items in the new row to the total item count.
            self.items += len(self.grid[index[0]])
       
        # Else if length of index is 2, a single item is being set.
        elif len(index) == 2:
            # If the item forces the row to be wider, change the width of
            # the whole grid.
            if index[1] >= self.width:
                self.width = index[1] + 1
          
            # Adjust the items count appropriately based on the change being made.
            if item is None:
                if index[1] in self.grid[index[0]]:
                    self.items -= 1
            else:
                if index[1] not in self.grid[index[0]]:
                    self.items += 1

            self.grid[index[0]][index[1]] = item

    def __str__(self):
        """"""
        pass

    def __len__(self):
        """Return the item count of the grid."""
        return self.items

    def capacity(self):
        """Return the area of the grid.
        
        The term "capacity" is misleading here since the grid will grow
        to whatever size it needs to be.
        """
        return self.width * self.height

    def sanitizeIndex(self, index):
        """Sanitize the provided index."""

        # Make index a list from either a tuple or a single integer.
        index = list(index) if isinstance(index, tuple) else [index]

        # If height is negative, make it positive.
        index[0] += self.height if index[0] < 0 else 0

        return index

    def makeList(self, gridRow):
        """Create a list from a dictionary of indexed items."""
        row = [None for item in range(self.width)]

        for item in gridRow.keys():
            row[item] = gridRow[item]
        
        return row
