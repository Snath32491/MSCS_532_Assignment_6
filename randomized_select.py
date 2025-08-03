import random

def randomized_partition(arr, pivot):
    """Partition array around pivot value."""
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    return lows, pivots, highs

def randomized_select(arr, k):
    """
    Select the k-th smallest element (1-based index) using Randomized Quickselect.
    Returns the k-th smallest element in the array.
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the length of the array")

    if len(arr) == 1:
        return arr[0]

    # Randomly select a pivot
    pivot = random.choice(arr)
    lows, pivots, highs = randomized_partition(arr, pivot)

    if k <= len(lows):
        return randomized_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))

# ----------------- Test Cases -----------------

if __name__ == "__main__":
    test_cases = [
        ([12, 3, 5, 7, 4, 19, 26], 3),       # Expected: 5
        ([1, 2, 3, 4, 5], 2),                # Expected: 2
        ([9, 8, 7, 6, 5], 5),                # Expected: 9
        ([7, 7, 7, 7, 7], 3),                # Expected: 7
        ([100, -1, 4, 2, 9, 0, 5], 4),       # Expected: 4
        ([5, 2, 9, 1, 2, 5, 3, 2, 5], 6),    # Expected: 5
        ([10], 1),                           # Expected: 10
    ]

    print("Randomized Quickselect Tests\n")
    for i, (arr, k) in enumerate(test_cases, 1):
        result = randomized_select(arr[:], k)
        print(f"Test #{i} - Array: {arr}, k = {k}")
        print(f"  k-th smallest element: {result}")
        print("-" * 50)
