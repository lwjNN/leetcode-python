from typing import List


def generate(numRows: int) -> List[List[int]]:
    res = []
    if numRows == 0:
        return res
    l = [1]
    res.append(l)
    if numRows == 1:
        return res
    l = [1, 1]
    res.append(l)
    if numRows == 2:
        return res

    for i in range(2, numRows):
        l = []
        for j in range(i+1):
            if j == 0 or j == i:
                l.append(1)
            else:
                l.append(res[i - 1][j - 1] + res[i - 1][j])
        res.append(l)
    return res


print(generate(6))
