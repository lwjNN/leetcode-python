class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        res = ""
        stack.append(s[0])
        for char in s[1:]:
            if not stack:
                stack.append(char)
            elif abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        while stack:
            res += stack.pop()
        return res[::-1]


s = Solution().makeGood("abBAcC")
print(s)
