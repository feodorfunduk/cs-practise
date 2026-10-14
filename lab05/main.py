from tablestats import *

name = input()
with open(name, encoding="utf-8") as table:
    rows = read_rows(table)
    print(len(rows))

    types = count_types(rows)
    print(len(types.keys()))
    
    minutes = total_minutes(rows, 'ошибка')
    print(minutes)
    
    counts = count_types(rows)
    
    
with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))
