from doubly_linked_list import DoublyLinkedList


def main():
    # Create a Doubly Linked List
    doubly_linked_list = DoublyLinkedList()

    # Testing the prepend method
    doubly_linked_list.prepend(3)
    doubly_linked_list.prepend(2)
    doubly_linked_list.prepend(1)

    # Testing the append method
    doubly_linked_list.append(4)
    doubly_linked_list.append(5)

    # Testing the insert_after method
    doubly_linked_list.insert_after(2, 2.5)

    # Testing the insert_before method
    doubly_linked_list.insert_before(4, 3.5)

    # Testing the delete method
    doubly_linked_list.delete(3)

    # Displaying the doubly linked list
    # doubly_linked_list.display()
    doubly_linked_list.display()

if __name__ == "__main__":
    main()
