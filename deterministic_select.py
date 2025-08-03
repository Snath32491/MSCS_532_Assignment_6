def partition(arr, pivot):
    """Partition array around the pivot value."""
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    return lows, pivots, highs

def deterministic_select(arr, k):
    """
    Select the k-th smallest element (1-based index) using the Median of Medians algorithm.
    Returns the k-th smallest element in the array (1 <= k <= len(arr)).
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the length of the array")
    
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Step 1: Divide arr into groups of 5 and find medians
    chunks = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    # Step 2: Find median of medians
    median_of_medians = deterministic_select(medians, len(medians) // 2 + 1)

    # Step 3: Partition around the pivot
    lows, pivots, highs = partition(arr, median_of_medians)

    if k <= len(lows):
        return deterministic_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return median_of_medians
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))

# ----------------- Test Cases -----------------

if __name__ == "__main__":
    test_cases = [
        ([12, 3, 5, 7, 4, 19, 26], 3),       # Expected: 5
        ([1, 2, 3, 4, 5], 2),                # Expected: 2
        ([9, 8, 7, 6, 5], 5),                # Expected: 9
        ([7, 7, 7, 7, 7], 3),                # Expected: 7
        ([100, -1, 4, 2, 9, 0, 5], 4),       # Expected: 4
        ([5, 2, 9, 1, 2, 5, 3, 2, 5], 6),    # Expected: 5 (with duplicates)
        ([10], 1),                           # Expected: 10 (single element)
    ]

    print("Deterministic Median of Medians Tests\n")
    for i, (arr, k) in enumerate(test_cases, 1):
        result = deterministic_select(arr[:], k)
        print(f"Test #{i} - Array: {arr}, k = {k}")
        print(f"  k-th smallest element: {result}")
        print("-" * 50)
