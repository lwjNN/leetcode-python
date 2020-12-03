class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    常规想法：将每个链表转为数字，求和。再把结果生成新的链表
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resNode = ListNode(-1, None)
        tmp = resNode

        def getNum(node: ListNode) -> int:
            index, res = 0
            while node:
                res += node.val * pow(10, index)
                index += 1
                node = node.next
            return res

        num1 = getNum(l1)
        print(num1)
        num2 = getNum(l2)
        print(num2)
        twoSum = num1 + num2
        sumStr = str(twoSum)
        result = sumStr[::-1]
        for ch in result:
            tmp.next = ListNode(int(ch))
            tmp = tmp.next
        return resNode.next

    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = resNode = ListNode(-1)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tmp.next = ListNode(s % 10)
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tmp = tmp.next
        return resNode.next
