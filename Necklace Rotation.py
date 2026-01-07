def rotate_necklace(arr, k):
    n = len(arr)
    k %= n
    return arr[k:] + arr[:k]


# ▶ Example Usage
print(rotate_necklace([1, 5, 3, 4, 2], 3))
print(rotate_necklace([10, 1, 2, 9, 8, 2], 5))