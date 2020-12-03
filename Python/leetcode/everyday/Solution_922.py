from _ast import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = []
        index = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                res.insert(index, A[i])
                index += 2
        index = 1
        for i in range(len(A)):
            if A[i] % 2 == 1:
                res.insert(index, A[i])
                index += 2
        return res
