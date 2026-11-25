import numpy as np

def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.asarray(matrix)
    return arr[row_start:row_stop, column_start:column_stop].tolist()


