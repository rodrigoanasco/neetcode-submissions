class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for e in tokens:
            if e == '+':
                stack.append(stack.pop() + stack.pop())
            elif e == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif e == '*':
                stack.append(stack.pop() * stack.pop())
            elif e == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            else:
                stack.append(int(e))
        
        return stack[0]