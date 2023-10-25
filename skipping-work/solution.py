def solution(x, y):
    for i in x:
        if i not in y:
            return i
        else:
            y.remove(i)

    return y.pop() if y else None
