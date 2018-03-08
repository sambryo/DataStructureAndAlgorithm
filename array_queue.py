class ArrayQueue(object):
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._queue = [None] * DEFAULT_CAPACITY
        self._size = 0
        self._first = 0

    def len(self):
        return len(self._queue)

    def is_empty(self):
        return len(self._queue) == 0

    def first(self):
        if self._queue.is_empty():
            raise Empty('queue is empty')
        return self._queue[self._first]

    def dequeue(self):
        if self._queue.is_empty():
            raise Empty('queue is empty')
        answer = self._queue[self._first]
        self._queue[self._first] = None  # helps with garbage collection
        self._first = (self._first + 1) % len(self._queue)
        self._size -= 1
        return answer

    # def enqueue
    # def resize
