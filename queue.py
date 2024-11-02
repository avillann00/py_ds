class queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, val):
        self.queue.append(val)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return
        self.queue.pop(0)

    def print_queue(self):
        if self.size == 0:
            return
        for i in self.queue:
            print(f'[{i}] -> ', end='')
        print('end')

my_queue = queue()
my_queue.print_queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
