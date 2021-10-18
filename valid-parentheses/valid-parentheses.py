class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for param in s:
            if param in ['(','[','{']:
                stack.append(param)
            else:
                if not stack:
                    return False
                item=stack.pop()
                if item=='(':
                    if param!=')':
                        return False
                if item=='[':
                    if param!=']':
                        return False
                if item=='{':
                    if param!='}':
                        return False
        return stack==[]