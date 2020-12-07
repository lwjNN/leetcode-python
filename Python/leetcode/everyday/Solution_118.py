"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def generate(numRows: int) -> List[List[int]]:
    res = []
    if not numRows:
        return res
    res.append([1])
    if numRows == 1:
        return res
    res.append([1, 1])
    if numRows == 2:
        return res
    for i in range(2, numRows):
        tmp = []
        tmp.append(1)
        for j in range(1, len(res[i-1])):
            tmp.append(res[i-1][j] + res[i-1][j-1])
        tmp.append(1)
        res.append(tmp)
    return res


print(generate(5))
