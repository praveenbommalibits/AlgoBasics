class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp._element, end=" ")
            temp = temp._next

    # Adding element at front
    def push(self, new_data):
        node = _Node(new_data, None)
        node._next = self.head
        self.head = node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Previous node must be in lined list ")
            return
        new_node = _Node(new_data, None)
        new_node._next = prev_node._next
        prev_node._next = new_node

    def append(self, new_data):
        append_node = _Node(new_data, None)
        if self.head is None:
            self.head = append_node
            return

        last = self.head
        while last._next:
            last = last._next
        last._next = append_node

    def delete_node(self, delete_ele):
        temp = self.head
        if temp is not None:
            if temp._element == delete_ele:
                self.head = temp._next
                return
        while temp:
            if temp._element == delete_ele:
                break
            prev = temp
            temp = temp._next

        if temp is None:
            return
        prev._next = temp._next
        temp = None

    # recursive implementation
    def delete_node_rec(self, head, delete_ele):
        if head is None:
            return
        if head._element == delete_ele:
            del_node = head
            head = head._next
            return
        self.delete_node_rec(head._next, delete_ele)

    def delete_pos(self, pos):
        if self.head is None:
            return

        temp = self.head
        if pos == 0:
            self.head = temp._next
            temp = None

        for i in range(pos - 1):
            temp = temp._next
            if temp is None:
                break
        if temp is None:
            print("Position limit is exceeded")
            return
        if temp._next is None:
            return

        next = temp._next._next
        temp._next = None
        temp._next = next

    def delete_ll(self):
        current = self.head
        while current:
            next = current._next
            del current.element
            current = next


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = _Node(1, None)
    second_node = _Node(2, None)
    third_node = _Node(3, None)

    llist.head._next = second_node
    second_node._next = third_node
    llist.printList()
    print()
    # insert at front
    llist.push(0)
    # insert in middle
    llist.insert_after(third_node, 4)
    # insert at end
    llist.append(5)

    llist.printList()

    llist.delete_node(9)
    print()
    llist.printList()

    print()
    # llist.delete_node_rec(llist.head, 4)
    llist.printList()

    print()
    llist.delete_pos(3)
    llist.printList()
    print()
    llist.delete_pos(8)
    llist.printList()
    print("\ndeletion complete linkedlist")
    llist.delete_ll()
    llist.printList()
