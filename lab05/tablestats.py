def read_rows(lines):
    res = []
    for i in list(lines)[1:]:
        if len(i.split(',')) == 3:
            res.append({'дата': i.split(',')[0], 'тип': i.split(',')[1],  'минуты': round(float(i.split(',')[2]), 1)})
        
    return res


def count_types(rows):
    res = dict()
    for i in rows:
        if i['тип'] in res.keys():
            res[i['тип']] += 1
        else:
            res[i['тип']] = 1
            
    return res
            
            
def total_minutes(rows, kind):
    res = 0.0
    for i in rows:
        if i['тип'] == kind:
            res += i['минуты']
            
    return res


def to_csv(counts):
    res = 'тип,количество\n'
    for k in sorted(counts.keys()):
        res += f'{k},{counts[k]}\n'
    
    return res


