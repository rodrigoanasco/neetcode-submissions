class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []
        print(self.stack)
    
    def push(self, val: int) -> None:
        
        if self.stack:
            if self.stack_min[-1] > val:
                self.stack_min.append(val)
            else:
                self.stack_min.append(self.stack_min[-1])
            self.stack.append(val)
        else:
            self.stack.append(val)
            self.stack_min.append(val)

        print(self.stack)
        print(self.stack_min)
        print("\n\n")

    def pop(self) -> None:
        self.stack.pop(-1)
        self.stack_min.pop(-1)
        
        print(self.stack)
        print(self.stack_min)
        print("\n\n")

    def top(self) -> int:
        return self.stack[-1]
        
        print(self.stack)
        print(self.stack_min)
        print("\n\n")

    def getMin(self) -> int:
        return self.stack_min[-1]
       
        print(self.stack)
        print(self.stack_min)
        print("\n\n")   
