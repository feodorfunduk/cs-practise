import numpy as np

hours = np.arange(0, 24, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("hours.shape:", hours.shape)
print("hours.ndim:", hours.ndim)
print("hours.size:", hours.size)
print("hours.dtype:", hours.dtype)


print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])



temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма (shape):", temperatures.shape)
print("Число измерений (ndim):", temperatures.ndim)
print("Число элементов (size):", temperatures.size)

print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2x2:\n", temperatures[0:2, 1:3])



matrix = np.arange(1, 26).reshape(5, 5)

slice_rows_3 = matrix[:3, :]
print("Первые три строки:\n", slice_rows_3)
print("Shape:", slice_rows_3.shape)

slice_rows_last2 = matrix[-2:, :]
print("Последние две строки:\n", slice_rows_last2)
print("Shape:", slice_rows_last2.shape)

slice_cols_2 = matrix[:, :2]
print("Первые два столбца:\n", slice_cols_2)
print("Shape:", slice_cols_2.shape)

slice_submatrix = matrix[1:4, 2:5]
print("Строки 1-3, столбцы 2-4:\n", slice_submatrix)
print("Shape:", slice_submatrix.shape)

slice_corner = matrix[-2:, -2:]
print("Угловой блок 2x2:\n", slice_corner)
print("Shape:", slice_corner.shape)



vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()

changed_hours[2:5] = 99
changed_hours[0::2] = -1

print("changed_hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()

changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("changed_matrix:\n", changed_matrix)
print("Исходный matrix:\n", matrix)

# Метод .copy() создает независимый дубликат массива, чтобы правки в новой копии не затронули оригинал.
# Без .copy() переменная changed_matrix стала бы просто ссылкой на те же данные в памяти, и менялись бы оба массива сразу.


numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers.shape:", numbers.shape)
print("table.shape:", table.shape)
print("transposed.shape:", transposed.shape)

# Преобразование reshape(3, 4) проходит успешно, так как количество ячеек совпадает с исходным: 3 * 4 = 12.
# Вариант reshape(5, 3) приведет к исключению ValueError: для такой сетки нужно 15 значений, а в массиве их всего 12.