from node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current

    def insert_after(self, target_data, data):
        node = Node(data)
        current = self.head
        while current:
            if current.data == target_data:
                if current.next:
                    node.next = current.next
                    current.next.prev = node
                    node.prev = current
                    current.next = node
                    return
                else:
                    current.next = node
                    node.prev = current
                    return
            current = current.next
        raise ValueError("The target_data is not present in the list.")

    def insert_before(self, target_data, data):
        node = Node(data)
        current = self.head
        while current:
            if current.data == target_data:
                if current.prev:
                    current.prev.next = node
                    node.prev = current.prev
                    node.next = current
                    return
                else:
                    self.head.prev = node
                    node.next = self.head
                    self.head = node
                    return
            current = current.next
        raise ValueError("The target_data is not present in the list.")

    def delete(self, data):
        if self.is_empty():
            raise ValueError("The list is empty.")
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current and current.data != data:
            current = current.next
        if current:
            current.prev.next = current.next
            current.next = current.prev
            return
        else:
            raise ValueError("The data is not present in the list.")

    def display(self):
        current = self.head
        while current:
            print(f"{current.data} <--> ", end='')
            current = current.next
