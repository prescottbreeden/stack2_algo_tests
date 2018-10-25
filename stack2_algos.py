# To run doctests, execute "python3 -m doctest -v stack2_algos.py"

# To learn more about each function, execute "help(function_name)" from
#   the python shell


# ===========================================
#           Basic Algorithm Tests
# ===========================================


def PrintKeysAndValues(obj):
    """
    Iterates through a dictionary and prints its keys and values.
    >>> obj = {"key": "value"}
    >>> PrintKeysAndValues(obj)
    key value
    """
    # for k, v in obj.items():
    #     print(k, v)
    for key in obj:
        print(key.value)


def ReverseArray(arr):
    """
    Reverses an array (in place) and returns it.
    >>> arr = [1, 2, 3, 4, 5]
    >>> ReverseArray(arr)
    [5, 4, 3, 2, 1]
    >>> arr = ['1', '2', '3', '4']
    >>> ReverseArray(arr)
    ['4', '3', '2', '1']
    """
    for i in range(int(len(arr)/2)):
        arr[i], arr[-(i+1)] = arr[-(i+1)], arr[i]
    return arr


# ===========================================
#           Singly Linked List Tests
# ===========================================


class SLNode:
    def __init__(self, val):
        """
        Instantiates a new node with value of 'val'.
        >>> node = SLNode(1)
        >>> node.val
        1
        """
        self.val = val
        self.next = None


class SLList:
    def __init__(self):
        """
        Instantiates an empty linked list with a 'head' pointing to None.
        >>> sll = SLList()
        >>> print(sll.head)
        None
        """
        self.head = None

    def AddToFront(self, val):
        """
        Adds a new node to the front of a Singly Linked List.
        >>> sll = SLList()
        >>> sll.AddToFront(1)
        >>> sll.AddToFront(2)
        >>> sll.AddToFront(3)
        >>> sll.AddToFront(4)
        >>> sll.PrintList()
        4
        3
        2
        1
        """
        node = SLNode(val)
        if (self.head):
            temp = self.head
            self.head = node
            self.head.next = temp
        else:
            self.head = node

    def AddToBack(self, val):
        """
        Adds a new node to the front of a Single Linked List.
        >>> sll = SLList()
        >>> sll.AddToBack(1)
        >>> sll.AddToBack(2)
        >>> sll.AddToBack(3)
        >>> sll.PrintList()
        1
        2
        3
        """
        node = SLNode(val)
        if (self.head):
            runner = self.head
            while(runner.next):
                runner = runner.next
            runner.next = node
        else:
            self.head = node

    def RemoveFromFront(self):
        """
        Moves the pointer for the current head to the second item
        >>> sll = SLList()
        >>> sll.AddToBack(1)
        >>> sll.AddToBack(2)
        >>> sll.AddToBack(3)
        >>> sll.RemoveFromFront()
        >>> print(sll.head.val)
        2
        """
        self.head = self.head.next

    def PrintList(self):
        """
        Prints the contents of a Singly Linked List to the terminal.
        >>> sll = SLList()
        >>> sll.AddToFront(3)
        >>> sll.PrintList()
        3
        """
        runner = self.head
        while(runner):
            print(runner.val)
            runner = runner.next


# ===============================
#           Stack Tests
# ===============================


class Stack:
    def __init__(self):
        """
        Instantiates an empty Stack.
        >>> stack = Stack()
        >>> stack.peek()
        'Stack is empty.'
        """
        self.arr = []
        self.size = 0

    def peek(self):
        """
        Returns the topmost value in the Stack.
        >>> stack = Stack()
        >>> stack.peek()
        'Stack is empty.'
        >>> stack.size
        0
        >>> stack.add('Rubber Baby Buggy Bumpers')
        >>> stack.peek()
        'Rubber Baby Buggy Bumpers'
        >>> stack.size
        1
        """
        if (self.isEmpty()):
            return "Stack is empty."
        else:
            return self.arr[-1]

    def isEmpty(self):
        """
        Evaluates if the Stack is empty, if it is, function returns True.
        If the stack is not empty, it returns False.
        >>> stack = Stack()
        >>> stack.isEmpty()
        True
        """
        if not self.arr:
            return True
        else:
            return False

    def add(self, item):
        """
        Adds an item to the Stack.
        >>> stack = Stack()
        >>> stack.add(1)
        >>> stack.peek()
        1
        >>> stack.add('hello')
        >>> stack.peek()
        'hello'
        """
        self.arr.append(item)
        self.size += 1

    def remove(self):
        """
        Removes the topmost item in the Stack.
        >>> stack = Stack()
        >>> stack.add(1)
        >>> stack.add('two')
        >>> stack.add(3)
        >>> stack.add('four')
        >>> stack.remove()
        >>> stack.peek()
        3
        >>> stack.size
        3
        >>> stack.remove()
        >>> stack.peek()
        'two'
        >>> stack.size
        2
        """
        self.arr.pop()
        self.size -= 1


# ===============================
#           Queue Tests
# ===============================


class Queue:
    def __init__(self):
        """
        Instantiates a Queue with a Singly Linked List.
        >>> q = Queue()
        >>> print(q.list.head)
        None
        """
        self.list = SLList()

    def enqueue(self, arg):
        """
        Adds an item to the end of the Queue.
        >>> q = Queue()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.enqueue(3)
        >>> q.enqueue(4)
        >>> print(q.list.head.val)
        1
        """
        self.list.AddToBack(arg)

    def dequeue(self):
        """
        Removes an item fron the front of the Queue.
        >>> q = Queue()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.dequeue()
        >>> print(q.list.head.val)
        2
        """
        self.list.RemoveFromFront()


# ========================================
#           Circular Queue Tests
# ========================================


class CircQueue:
    def __init__(self, capacity):
        """
        Instantiates an empty Circular Queue with a capacity of 'capacity'
        >>> cq = CircQueue(5)
        >>> cq.capacity
        5
        """
        self.arr = []
        self.capacity = capacity

    def enqueue(self, arg):
        """
        Adds an item to the Circular Queue if capacity is not met. If the
        Circular Queue is at max capacity the function returns an error.
        >>> cq = CircQueue(5)
        >>> cq.enqueue(1)
        >>> cq.enqueue(2)
        >>> cq.enqueue(3)
        >>> cq.arr[0]
        1
        """
        if (len(self.arr) < self.capacity):
            self.arr.append(arg)
        else:
            raise AttributeError('Queue is full.')

    def dequeue(self):
        """
        Removes the oldest item from the Circular Queue. If the Circular Queue
        is empty the function returns an error.
        >>> cq = CircQueue(5)
        >>> cq.enqueue(1)
        >>> cq.enqueue(2)
        >>> cq.dequeue()
        >>> cq.arr[0]
        2
        """
        if self.arr:
            self.arr.pop(0)
        else:
            raise AttributeError('Queue is empty.')
