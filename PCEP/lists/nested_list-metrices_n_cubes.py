# /usr/local/bin/python3.8

# Matrix (lists that have lists of their own - 2D)

# Two lists --> matrix
'''
1 2 3
4 5 6
'''

# note: these are two lists ontop of each other. To add them, they had to have the same length (no. column)

my_matrix = [ [ 1, 2, 3 ], [4, 5, 6] ]      # a list with a list
print ( my_matrix )                         # [[1, 2, 3], [4, 5, 6]]

row_count = len(my_matrix)                  # counts number of units (i.e. rows) in the top outter list
print ( row_count )

column_count = len(my_matrix[0])            # counts number of unit on each list (i.e. column) in the nested list
print ( column_count )                      # because column is length and each list must have same length - just count length of one list

single_unit = my_matrix[0][0]               # first list (first unit in the outter list) and
print ( single_unit )                       # first unit in the nested list = 1

last_unit = my_list[1][2]
print ( last_unit )                         # 6


# TYPES OF MATRICES

### 2 X 2  matrix (two rows, two columns)
'''
1 2
3 4
'''

### cube matrix ( no. rows == no. column)

# e.g 3 cube
'''
1 2 3
4 5 6
7 8 9
'''