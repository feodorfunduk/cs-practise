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
