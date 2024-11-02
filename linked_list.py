class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_head(self, val):
        new = node(val)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.head.prev = new
            new.next = self.head
            self.head = new

    def add_tail(self, val):
        new = node(val)
        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

    def remove_head(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def remove_tail(self):
        if self.tail is None:
            return 
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def remove_val(self, val):
        if self.head is None:
            return
        if self.head.data == val:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return
        temp = self.head
        while temp is not None:
            if temp.data == val:
                temp.prev.next = temp.next
            temp = temp.next

    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        while temp is not None:
            print(f'[{temp.data}] -> ', end='')
            temp = temp.next
        print('end')

myll = linked_list()
myll.print_list()
myll.add_head(1)
myll.print_list()
myll.add_tail(5)
myll.print_list()
myll.add_head(70)
myll.print_list()
myll.remove_head()
myll.print_list()
myll.remove_tail()
myll.print_list()
myll.remove_val(1)
myll.print_list()
