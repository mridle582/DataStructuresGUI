class MyStack:
    
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, value):
        self.top += 1
        self.stack.insert(self.top, value) 

    def pop(self):
        if(self.top == -1):
            return 'Stack is empty.'
        old_top = self.stack[self.top]
        self.top -= 1
        return old_top

    def peek(self):
        if (self.top == -1):
            return 'The stack is empty'
        return self.stack[self.top]

    def toString(self):
        output = '\n'
        for i in range(self.top):
            output += '\n' + str(self.stack[i])
        return output[::-1]




    