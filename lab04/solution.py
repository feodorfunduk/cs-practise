def winner(names: list[str], scores: list[float]) -> str:
    best = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best]:
            best = i
    return names[best]

def average(scores: list[float]) -> float:
    return round(sum(scores) / len(scores), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    s = list(range(len(names)))
    order = sorted(s, key=lambda i: scores[i], reverse=True)
    res = []
    for i in order:
        res.append(names[i])
    return res

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    res = []
    for i in range(len(names)):
        if scores[i] > avg
            res.append(names[i])
    return res
