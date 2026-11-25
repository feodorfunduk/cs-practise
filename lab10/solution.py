import numpy as np

def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()


