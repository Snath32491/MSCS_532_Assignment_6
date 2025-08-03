# -------------------------
# Arrays and Matrices
# -------------------------

class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size

    def insert(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value

    def delete(self, index):
        if 0 <= index < self.size:
            self.data[index] = None

    def access(self, index):
        if 0 <= index < self.size:
            return self.data[index]

    def __str__(self):
        return str(self.data)


class Matrix:
    def __init__(self, rows, cols):
        self.data = [[0] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        self.data[row][col] = value

    def access(self, row, col):
        return self.data[row][col]

    def __str__(self):
        return '\n'.join(str(row) for row in self.data)


# -------------------------
# Stack (using Array)
# -------------------------

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)


# -------------------------
# Queue (using Array)
# -------------------------

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def front(self):
        return self.queue[0] if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)


# -------------------------
# Singly Linked List
# -------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next

    def traverse(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def __str__(self):
        return "->".join(str(x) for x in self.traverse())


# -------------------------
# Test / Demo
# -------------------------

def main():
    print("=== Array ===")
    arr = Array(5)
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.delete(0)
    print("Array contents:", arr)

    print("\n=== Matrix ===")
    mat = Matrix(2, 2)
    mat.insert(0, 0, 5)
    mat.insert(1, 1, 10)
    print("Matrix contents:")
    print(mat)

    print("\n=== Stack ===")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Stack after pushes:", stack)
    print("Popped from stack:", stack.pop())
    print("Top of stack:", stack.peek())

    print("\n=== Queue ===")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print("Queue after enqueues:", queue)
    print("Dequeued from queue:", queue.dequeue())
    print("Front of queue:", queue.front())

    print("\n=== Singly Linked List ===")
    ll = SinglyLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    print("Linked list after inserts:", ll)
    ll.delete(2)
    print("Linked list after deleting 2:", ll)


if __name__ == "__main__":
    main()
