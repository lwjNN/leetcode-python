class Solution:
    def isValid(self, s: str) -> bool:
        if s and len(s) == 0:
            return True
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                elif (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[') or (
                        char == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    stack.append(char)
        if not stack:
            return True
        return False
