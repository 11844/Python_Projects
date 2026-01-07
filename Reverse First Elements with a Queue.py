from collections import deque


def reverse_first_k(queue, k):

    stack = []

    for _ in range(k):
        stack.append(queue.popleft())


    while stack:
        queue.append(stack.pop())


    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

    return queue



# ▶ Example Usage
jls_extract_var = 5
q = deque([1, 2, 3, 4, jls_extract_var])

k = 3

print(list(reverse_first_k(q, k)))

