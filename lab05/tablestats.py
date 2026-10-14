def read_rows(lines):
    res = []
    header = None
    for line in lines:
        line = line.strip() 
        if not line:
            continue

        parts = [s.strip() for s in line.split(',')]
        if header is None:
            header = parts
        elif len(parts) == len(header):
            res.append(dict(zip(header, parts))) 
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
            try:
                res += float(i['минуты'])
            except Exception as e:
                continue
            
    return round(res, 1)


def to_csv(counts):
    res = 'тип,количество\n'
    for k in sorted(counts.keys()):
        res += f'{k},{counts[k]}\n'
    
    return res

