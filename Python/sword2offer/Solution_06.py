"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
 
示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[:: -1]

    def reversePrint_res(self, head: ListNode) -> List[int]:
        return self.reversePrint_res(head.next) + [head.val] if head else []

