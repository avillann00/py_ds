class stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val):
        self.stack.append(val)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        self.stack.pop()

    def peek(self):
        if self.size == 0:
            return 
        return self.stack[-1]

    def print_stack(self):
        if self.size == 0:
            return  
        for i in range(self.size):
            print(f'[{self.stack[-(i + 1)]}]')
            print('|')
            print('v')
        print('end')
        print()

my_stack = stack()
my_stack.print_stack()
my_stack.push(1)
my_stack.print_stack()
my_stack.push(2)
my_stack.push(3)
my_stack.print_stack()
print(my_stack.peek())
my_stack.pop()
