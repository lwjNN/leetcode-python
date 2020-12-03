from typing import List


def maximumWealth(self, accounts: List[List[int]]) -> int:
    result = 0
    for i in range(len(accounts)):
        result = max(result, sum(accounts[i]))
    return result

print(maximumWealth([[1,3], [2,4]]))