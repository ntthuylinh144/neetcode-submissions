mapping = {
    ')': '(',
    '}': '{',
    ']': '['
}

class Solution:
        def isValid(self, s: str) -> bool:
                if len(s)%2== 1: return False
                stack = []
                for v in s:
                    if v in mapping:
                        if not stack:
                            return False
                        top = stack.pop()
                        if top != mapping[v]:
                            return False
                    else:
                        stack.append(v)
                return len(stack)==0