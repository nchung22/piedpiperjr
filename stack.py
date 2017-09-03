class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        link = Link(value)
        link.next = self.head
        self.head = link

    def pop(self):
        link = self.head
        if link is None:
            return None
        self.head = link.next
        return link.value


class Link:
    def __init__(self, value):
        self.next = None
        self.value = value


def main():
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

if __name__ == "__main__":
    main()