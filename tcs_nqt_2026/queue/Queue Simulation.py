# Problem

# You are given Q operations on a queue.

# Operations can be:

# ENQUEUE X
# DEQUEUE
# FRONT
# SIZE
# ISEMPTY

# Rules

# ENQUEUE X → Insert X
# DEQUEUE → Remove front and print it
# FRONT → Print front element
# SIZE → Print size of queue
# ISEMPTY → Print True or False
# If queue is empty:
# DEQUEUE → print -1
# FRONT → print -1
# Example Input
# 8
# ENQUEUE 5
# ENQUEUE 10
# FRONT
# DEQUEUE
# FRONT
# SIZE
# ISEMPTY
# DEQUEUE

from collections import deque

def solve():
    n = int(input())
    q = deque()

    for _ in range(n):
        operation = input().split()

        if operation[0] == "ENQUEUE":
            q.append(int(operation[1]))

        elif operation[0] == "DEQUEUE":
            print(q.popleft() if q else -1)

        elif operation[0] == "FRONT":
            print(q[0] if q else -1)

        elif operation[0] == "SIZE":
            print(len(q))

        elif operation[0] == "ISEMPTY":
            print(len(q) == 0)

solve()
    