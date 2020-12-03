from typing import List


def plusOne(digits: List[int]) -> List[int]:
    num_s = "".join([str(x) for x in digits])
    res = str(int(num_s) + 1)
    r = [int(x) for x in res]
    return [0]*(len(digits)-len(r)) + r
print(plusOne([9,9,9]))