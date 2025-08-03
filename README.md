Assignment 6
Part 1: Selection Algorithms: Deterministic vs Randomized

This project implements and analyzes two core selection algorithms for finding the **k-th smallest element** (also known as order statistics) in an unsorted array.

Implemented Algorithms

1. Deterministic Selection (Median of Medians)
- Guarantees worst-case linear time: `O(n)`
- Divides the array into groups of 5, recursively selects a good pivot.
- Robust even on adversarial inputs.

2. Randomized Selection (Quickselect)
- Expected linear time: `O(n)`
- Similar to QuickSort but only recurses on one partition.
- Simpler and faster in practice, but worst-case is `O(n²)`.

Features

- Handles arrays with duplicates
- Empirically benchmarks both algorithms on:
  - Random arrays
  - Sorted arrays
  - Reverse-sorted arrays
- Measures execution time for various input sizes and `k` values

Outputs

- Generates performance plots for:
  - Deterministic vs Randomized Selection
  - Across different array types and sizes

How to Run

Ensure Python is installed and dependencies are met.

Install dependencies
```bash
pip install matplotlib numpy


Part 2: Elementary Data Structures: Implementation and Analysis

This project contains Python implementations and a detailed analysis of fundamental data structures, including:

- Arrays and Matrices  
- Stacks (LIFO)  
- Queues (FIFO)  
- Singly Linked Lists  

A formal report with performance analysis, trade-offs, and real-world applications is also provided.

Implemented Structures

Array
- Operations: Insert, Delete, Access
- Fixed-size implementation with manual indexing

Matrix
- 2D array (list of lists)
- Supports direct element access and insertion

Stack (using array)
- Operations: Push, Pop, Peek
- Built with Python list (`append`/`pop`)

Queue (using array)
- Operations: Enqueue, Dequeue, Front
- Uses `append()` and `pop(0)` — simple, but not optimized

Singly Linked List
- Node-based implementation
- Operations: Insert (head), Delete (by value), Traverse


How to Run

1. Open a terminal or IDE.
2. Run the Python script:
   ```bash
   python data_structures.py

