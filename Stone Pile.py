from collections import deque

def stone_pile_game(test_cases):
    results = []
    for A in test_cases:
        pile = deque(A)
        aman_turn = True

        while len(pile) > 1:
            if aman_turn:
                pile.append(pile.popleft())  # move 1
                pile.popleft()               # move 2
            else:
                pile.append(pile.popleft())  # move 1
                pile.append(pile.popleft())  # move 1
                pile.popleft()               # move 2
            aman_turn = not aman_turn

        last_player = 0 if aman_turn else 1
        results.append((last_player, pile[0]))
    return results


# ▶ Example Usage
test_cases = [
    [-5, 0, 5],
    [-1, -3, 2, 4],
    [-100000, 0, 0, 100000, -1000000, 1000000]
]

output = stone_pile_game(test_cases)
for result in output:
    print(result)
