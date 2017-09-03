from stack import Link


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,value):
        link = Link(value)
        if self.head is None:
            self.head = link
        if self.tail is not None:
            self.tail.next = link
        self.tail = link

    def dequeue(self):
        link = self.head
        if link is None:
            return None
        self.head = link.next
        if self.head is None:
            self.tail = None
        return link.value


def main():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

main()


