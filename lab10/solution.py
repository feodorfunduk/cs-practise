import numpy as np

def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.asarray(matrix)
    return arr[row_start:row_stop, column_start:column_stop].tolist()


def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    dtype = float if isinstance(value, float) else None
    arr = np.asarray(matrix, dtype=dtype).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()


def matrix_vector_product(matrix, vector):
    return (np.array(matrix) @ np.array(vector)).tolist()


def matrix_multiply(left, right):
    return (np.array(left) @ np.array(right)).tolist()


def transpose_matrix(matrix):
    return np.array(matrix).T.tolist()


def solve_system(matrix, vector):
    solution = np.linalg.solve(
        np.array(matrix, dtype=float), np.array(vector, dtype=float)
    )
    return np.round(solution, 6).tolist()


def tensor_channel_mean(tensor):
    return np.array(tensor, dtype=float).mean(axis=-1).tolist()


def point_distance(first, second):
    distance = np.linalg.norm(
        np.array(first, dtype=float) - np.array(second, dtype=float)
    )
    return round(float(distance), 6)
