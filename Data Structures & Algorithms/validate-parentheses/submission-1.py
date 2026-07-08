class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keys = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            
            if c in keys:
                if stack and stack[-1] == keys[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        

        # 'stack' by its own returns true if it's full, so saying 'not stack', means 'not full'
        if not stack:
            return True
        else:
            return False

