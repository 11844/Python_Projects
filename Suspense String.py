from collections import deque

def suspense_string(s):
    S = deque(s)
    T = deque()
    alice_turn = True

    while S:
        if alice_turn:
            c = S.popleft()
            if not T or c < T[0]:
                T.appendleft(c)
            else:
                T.append(c)
        else:
            c = S.pop()
            if not T or c > T[0]:
                T.appendleft(c)
            else:
                T.append(c)
        alice_turn = not alice_turn

    return "".join(T)


# ▶ Example Usage
inputs = ["10", "0001", "010111", "1110000010"]
for s in inputs:
    print(suspense_string(s))
