def show(linkedgrid):
    """
    Print the values inside a linked grid, row by row.
    Values in each row are separated by spaces.
    """
    row = linkedgrid.head

    while row is not None:
        node = row
        values = []

        while node is not None:
            values.append(str(node.data))
            node = node.nextX

        print(" ".join(values))
        row = row.nextY



def fetch(linked_grid, i, j):
    """
    Return the value at the (i, j) position of the grid.
    Uses 1-based indexing, as required.
    """
    # Move down to row i
    row = linked_grid.head
    for _ in range(1, i):
        row = row.nextY

    # Move right to column j
    node = row
    for _ in range(1, j):
        node = node.nextX

    return node.data



def hor_cat(grid_a, grid_b):
    """
    Horizontally concatenate grid_b onto grid_a.
    That is: attach each row of B to the end of the corresponding row of A.
    Grid A is modified and returned.
    """
    row_a = grid_a.head
    row_b = grid_b.head

    while row_a is not None and row_b is not None:

        # Find the last node in this row of A
        end = row_a
        while end.nextX is not None:
            end = end.nextX

        # Attach the row from grid B
        end.nextX = row_b

        # Move to next row
        row_a = row_a.nextY
        row_b = row_b.nextY

    # Update grid width
    grid_a.sizeX += grid_b.sizeX
    return grid_a



def smart_hor_cat(grid_a, grid_b):
    """
    Same as hor_cat, but uses the tail pointers for efficiency.
    Works only for LinkedGridWithTails.
    """
    right_col = grid_a.tailX     # top-right of A
    left_col = grid_b.head       # top-left of B

    # Connect matching rows
    while right_col is not None and left_col is not None:
        right_col.nextX = left_col
        right_col = right_col.nextY
        left_col = left_col.nextY

    # Update tails of the modified grid
    grid_a.tailX = grid_b.tailX        # new top-right
    grid_a.tailXY = grid_b.tailXY      # new bottom-right
    # tailY (bottom-left) remains unchanged

    grid_a.sizeX += grid_b.sizeX
    return grid_a



def transpose(grid):
    # Step 1: collect all nodes in a 2D list for easy access
    table = []
    row = grid.head

    while row is not None:
        row_nodes = []
        node = row

        while node is not None:
            row_nodes.append(node)
            node = node.nextX

        table.append(row_nodes)
        row = row.nextY

    height = len(table)
    if height == 0:
        return grid

    width = len(table[0])

    # Step 2: rewire pointers for the transpose
    for r in range(height):
        for c in range(width):
            node = table[r][c]

            # nextX becomes "down" -> move from row r to r+1
            node.nextX = table[r + 1][c] if r + 1 < height else None

            # nextY becomes "right" -> move from col c to c+1
            node.nextY = table[r][c + 1] if c + 1 < width else None

    # Step 3: update grid dimensions
    grid.sizeX = height
    grid.sizeY = width

    # Step 4: update tail pointers for the new shape
    grid.tailX = table[height - 1][0]            # new top-right
    grid.tailY = table[0][width - 1]             # new bottom-left
    grid.tailXY = table[height - 1][width - 1]   # new bottom-right

    return grid



def element_wise_add(grid_a, grid_b):
    row_a = grid_a.head
    row_b = grid_b.head

    while row_a is not None and row_b is not None:
        node_a = row_a
        node_b = row_b

        while node_a is not None and node_b is not None:
            node_a.data += node_b.data
            node_a = node_a.nextX
            node_b = node_b.nextX

        row_a = row_a.nextY
        row_b = row_b.nextY

    return grid_a
