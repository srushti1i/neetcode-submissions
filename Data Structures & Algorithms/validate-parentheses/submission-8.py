class Solution:
    def isValid(self, s: str) -> bool:
        d={']': '[', '}': '{', ')': '('}
        stack=[]
        for c in s:
            if c in d:
                if not stack:
                    return False
                char=stack.pop()
                if d[c]!=char:
                    return False
            else:
                stack.append(c)
        return not stack