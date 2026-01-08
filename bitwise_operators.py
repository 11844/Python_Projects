def demonstrate_bitwise_operators():
    # Define two integers
    a = 10  # Binary: 1010
    b = 4   # Binary: 0100

    print(f"Initial values:")
    print(f"a = {a} (Binary: {bin(a)})")
    print(f"b = {b} (Binary: {bin(b)})")
    print("-" * 40)

    # Bitwise AND (&)
    # Sets each bit to 1 if both bits are 1
    # 1010
    # 0100
    # ----
    # 0000 -> 0
    bitwise_and = a & b
    print(f"a & b  (AND)        : {bitwise_and} \t(Binary: {bin(bitwise_and)})")

    # Bitwise OR (|)
    # Sets each bit to 1 if one of two bits is 1
    # 1010
    # 0100
    # ----
    # 1110 -> 14
    bitwise_or = a | b
    print(f"a | b  (OR)         : {bitwise_or} \t(Binary: {bin(bitwise_or)})")

    # Bitwise XOR (^)
    # Sets each bit to 1 if only one of two bits is 1
    # 1010
    # 0100
    # ----
    # 1110 -> 14
    bitwise_xor = a ^ b
    print(f"a ^ b  (XOR)        : {bitwise_xor} \t(Binary: {bin(bitwise_xor)})")

    # Bitwise NOT (~)
    # Inverts all the bits
    # Returns one's complement of the number -> -(x + 1)
    # ~10 = -11
    bitwise_not_a = ~a
    print(f"~a     (NOT)        : {bitwise_not_a} \t(Binary: {bin(bitwise_not_a)})")

    # Bitwise Left Shift (<<)
    # Shift left by pushing zeros in from the right and let the leftmost bits fall off
    # 10 (1010) << 2 -> 101000 -> 40
    left_shift = a << 2
    print(f"a << 2 (Left Shift) : {left_shift} \t(Binary: {bin(left_shift)})")

    # Bitwise Right Shift (>>)
    # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
    # 10 (1010) >> 1 -> 0101 -> 5
    right_shift = a >> 1
    print(f"a >> 1 (Right Shift): {right_shift} \t(Binary: {bin(right_shift)})")

if __name__ == "__main__":
    demonstrate_bitwise_operators()
