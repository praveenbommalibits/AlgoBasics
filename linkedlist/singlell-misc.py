class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class Singlell_misc:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = _Node(new_data, None)
        new_node._next = self.head
        self.head = new_node

    def get_nth_node(self, nth):
        if self.head is None:
            print("Lined list was empty")
            return
        temp = self.head
        count = 0
        while temp:
            if count == nth:
                return temp._element
            count += 1
            temp = temp._next
        print("Specified nth element not availabe in ll")
        return

    def get_nth(self, llist, nth):
        llist.get_nth_rec(self.head, nth, llist)

    def get_nth_rec(self, head, nth, llist):
        count = 0
        if count == nth:
            print(head._element)
        else:
            llist.get_nth_rec(head._next, nth-1, llist)

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp._element, end=" ")
            temp = temp._next


if __name__== '__main__':
    singlell = Singlell_misc()
    singlell.push(12)
    singlell.push(23)
    singlell.push(1)
    singlell.push(48)
    singlell.push(76)
    singlell.push(14)

    singlell.print_ll()
    print("\n3rd element: ", singlell.get_nth_node(3))
    print("nth node rec")
    singlell.get_nth(singlell, 3)





