from typing import List


def getRow(rowIndex: int) -> List[int]:
    pre = []
    for i in range(rowIndex+1):
        cur = []
        for j in range(i + 1):
            if j == 0 or j == i:
                cur.append(1)
            else:
                cur.append(pre[j - 1] + pre[j])
        pre = cur
    return cur

print(getRow(3))