import grid

example = grid.Grid()

# Assign items using a [y, x] indexing scheme.
example[0, 0] = 'hello'
example[0, 1] = 'world'

# Assign entire rows.
example[1] = [x for x in range(5)]
example[2] = 3.1415926
example[3] = ('a', 'b', 'c')

# Assign really far out of bounds because why not?
example[1, 6] = True

# Even assign backwards!
example[-1, -3] = False
example[-2, 1] = 'crazy right?'

print(example)
print('\nSize is {0}'.format(len(example)))
print('Capacity is {0}'.format(example.capacity()))

# Removing stuff works just fine too.
example[1, 2] = None
example[-1] = []

print(example)
print('\nSize is {0}'.format(len(example)))
print('Capacity is {0}'.format(example.capacity()))
