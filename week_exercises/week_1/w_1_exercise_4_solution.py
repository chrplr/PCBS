"""
Pascal's triangle

Write a function to compute the first n rows of Pascal's triangle
(see: <https://en.wikipedia.org/wiki/Pascal%27s_triangle>).

For this exercise, you are responsible for testing that your solution yields
correct outputs and handles unexpected inputs gracefully.
You can do it!
"""

def get_pascal_triangle_rows(n_rows):
    rows = []
    last_row = []
    for i in range(n_rows):
        row = get_pascal_triangle_next_row(last_row)
        rows.append(row)
        last_row = row
    return rows

def get_pascal_triangle_next_row(last_row):
    if len(last_row) == 0:
        row = [1]
    else:
        left_values = [0] + last_row
        right_values = last_row + [0]
        row = [ x + y for x, y in zip(left_values, right_values) ]
    return row

# Tests
assert get_pascal_triangle_rows(0) == []
rows = get_pascal_triangle_rows(8)
assert rows[7] == [1, 7, 21, 35, 35, 21, 7, 1]
print(rows)
