porog = int(input('Введите порог: '))
n = int(input('Введите количество записей: '))
q = []
errors = 0
prev = 0

for i in range(n):
    t = input('Введите температуру: ')
    if t == 'error':
        errors += 1
    elif float(t) > porog:
        prev += 1
        q.append(float(t))
    else:
        q.append(float(t))

print(f'Сколько записей пришло всего: {n}\nсколько среди них ошибок: {errors}\nсколько превышений: {prev}\nмаксимальное показание: {max(q):.1f}\nсреднее показание: {sum(q) / len(q):.1f}')

