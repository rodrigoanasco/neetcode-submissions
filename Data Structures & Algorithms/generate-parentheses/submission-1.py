class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # You can only put an open parenthesis if n > parenthesis
        # open must be < n
        # closed must be < open


        opened = 0
        closed = 0
        temp = []
        final = []
        def recursive_parenthesis(opened, closed):
            
            if closed == opened == n:
                final.append("".join(temp))
                return
            
            if opened < n:
                temp.append("(")
                recursive_parenthesis(opened + 1, closed)
                temp.pop()

            if closed < opened:
                temp.append(")")
                recursive_parenthesis(opened, closed + 1)
                temp.pop()
        
        recursive_parenthesis(0, 0)
        return final