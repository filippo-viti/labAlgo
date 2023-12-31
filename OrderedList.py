class OrderedList:
    class Node:
        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None

    def __str__(self):
        r = ''
        if self.head is not None:
            current = self.head
            while current is not None:
                r += str(current.value) + ' '
                current = current.next
        return r

    def insert(self, value):
        new_node = self.Node(value)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        elif self.head.value > value:
            new_node.next = self.head
            self.head = new_node

        else:
            current = self.head
            while current.next is not None and value > current.next.value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def os_select(self, i):
        current = self.head
        while current is not None and i != 0:
            current = current.next
            i -= 1
        return current

    def os_rank(self, x):
        current = self.head
        i = 0
        while current is not None and current.value != x:
            current = current.next
            i += 1
        return i
