import numpy as np


def reshape_rows(values: list, width: int) -> list:
    array = np.asarray(values, dtype=float)
    if array.size % width != 0 or width <= 0:
        return []
    table = array.reshape(-1, width)
    return table.tolist()


def block(matrix: list, rows: list, columns: list) -> list:
    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return []
    selected = array[np.ix_(rows, columns)]
    return selected.tolist()


def column_means(matrix: list) -> list:
    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return []
    meannn = np.mean(array, axis=0)
    roundud = np.round(meannn, 6)
    return roundud.tolist()


def column_range(matrix: list, column: int) -> float:
    array = np.asarray(matrix, dtype=float)
    if array.size == 0:
        return 0.0
    values = array[:, column]
    spread = np.max(values) - np.min(values)
    return float(np.round(spread, 6))
