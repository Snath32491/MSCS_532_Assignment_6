import random
import time
import matplotlib.pyplot as plt
import tracemalloc
import numpy as np

# ---------------- RANDOMIZED QUICKSELECT ----------------
def randomized_partition(arr, pivot):
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    return lows, pivots, highs

def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    lows, pivots, highs = randomized_partition(arr, pivot)
    if k <= len(lows):
        return randomized_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))

# ---------------- DETERMINISTIC SELECT ----------------
def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k-1]
    
    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(group)[len(group)//2] for group in groups]
    pivot = deterministic_select(medians, len(medians)//2 + 1)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k <= len(lows):
        return deterministic_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))

# ---------------- TESTING FUNCTION ----------------
def run_with_metrics(algorithm, arr, k):
    times = []
    memories = []
    for _ in range(5):
        arr_copy = arr[:]
        tracemalloc.start()
        start = time.perf_counter()
        algorithm(arr_copy, k)
        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append(end - start)
        memories.append(peak / 1024)  # Convert to KB
    return np.mean(times), np.max(memories)

# ---------------- EMPIRICAL ANALYSIS ----------------
def empirical_analysis():
    sizes = [100, 500, 1000, 2000, 5000, 10000]
    distributions = ['Random', 'Sorted', 'Reverse Sorted']

    data = {
        'Randomized Quickselect': {d: {'time': [], 'memory': []} for d in distributions},
        'Deterministic Median of Medians': {d: {'time': [], 'memory': []} for d in distributions}
    }

    for size in sizes:
        base_array = list(range(1, size + 1))
        k = size // 2

        # Generate input variants
        inputs = {
            'Random': random.sample(base_array, len(base_array)),
            'Sorted': base_array[:],
            'Reverse Sorted': base_array[::-1]
        }

        for dist_type, array in inputs.items():
            print(f"Testing {size} elements - {dist_type}")

            # Randomized Quickselect
            time_qs, mem_qs = run_with_metrics(randomized_select, array, k)
            data['Randomized Quickselect'][dist_type]['time'].append(time_qs)
            data['Randomized Quickselect'][dist_type]['memory'].append(mem_qs)

            # Deterministic Select
            time_dm, mem_dm = run_with_metrics(deterministic_select, array, k)
            data['Deterministic Median of Medians'][dist_type]['time'].append(time_dm)
            data['Deterministic Median of Medians'][dist_type]['memory'].append(mem_dm)

    # Plotting
    plot_results(sizes, data)

# ---------------- PLOTTING FUNCTION ----------------
def plot_results(sizes, data):
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))

    # Execution Time Plot
    for algo in data:
        for dist in data[algo]:
            axs[0].plot(sizes, data[algo][dist]['time'], label=f'{algo} - {dist}', marker='o')
    axs[0].set_title('Execution Time vs Input Size')
    axs[0].set_xlabel('Input Size (n)')
    axs[0].set_ylabel('Average Time (s)')
    axs[0].legend()
    axs[0].grid(True)

    # Memory Usage Plot
    for algo in data:
        for dist in data[algo]:
            axs[1].plot(sizes, data[algo][dist]['memory'], label=f'{algo} - {dist}', marker='x')
    axs[1].set_title('Peak Memory Usage vs Input Size')
    axs[1].set_xlabel('Input Size (n)')
    axs[1].set_ylabel('Memory (KB)')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()

# ---------------- MAIN ----------------
if __name__ == "__main__":
    empirical_analysis()
