"""
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
返回尽可能高的分数。

示例：
输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 
提示：

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] 是 0 或 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/score-after-flipping-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def matrixScore(A: List[List[int]]) -> int:
    r = len(A)
    c = len(A[0])

    def changeRow(arr: List[int]) -> List:
        for i in range(len(arr)):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
        return arr

    # 将每一行的第一列不为1的该行逆转
    for i in range(r):
        if A[i][0] == 0:
            changeRow(A[i])

    def getSum(A: List[List[int]]) -> int:
        total = 0
        for i in range(r):
            s = ""
            for j in A[i]:
                s += str(j)
            tmp = int(s, 2)
            total += tmp
        return total

    result = getSum(A)

    tmpList = []
    for i in range(c-1, 0, -1):
        zero = 0
        one = 0
        for j in range(r):
            if (A[j][i] == 0):
                zero += 1
            else:
                one += 1
        tmpList.append(one - zero)
    for i in range(len(tmpList)):
        if tmpList[i] < 0:
            result += abs(tmpList[i]) * (2 ** i)
    return result


print(matrixScore([[0,1],[0,1],[0,1],[0,0]]))
print(matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
