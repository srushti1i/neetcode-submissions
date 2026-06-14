class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'}':'{', ']':'[', ')':'('}
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if i in d and d[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        print(stack)
        return len(stack) == 0