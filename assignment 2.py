# ==============================================================================
#                  DATA STRUCTURES LABORATORY REPORT
#          IMPLEMENTATION OF SINGLY LINKED LIST & THEORY ANSWERS
# ==============================================================================
# Submitted by: [GAIUS DESTINY DIVINE]
# Matric No:    [230502094]
# Department:   Computer Science
# course code:        CSC 301
# course title:      Data Structures
# ==============================================================================


# DSA Assignment - All Questions Solved
# Arrays, Recursion, Linear Search, Binary Search

# -------------------------------------------------
# 1) Sum of first 10 natural numbers using RECURSION
# -------------------------------------------------
def sum_first_n(n):
    if n == 0:
        return 0
    return n + sum_first_n(n - 1)

print("1) Sum of first 10 natural numbers (using recursion):")
print(sum_first_n(10))  # Output: 55


# -------------------------------------------------
# 2) Fibonacci series up to 8th term using a program + dynamic array (list)
# -------------------------------------------------
def fibonacci_series(n):
    fib = [0, 1]  # First two terms
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

print("\n2) Fibonacci series (first 8 terms):")
print(fibonacci_series(8))  
# Output: [0, 1, 1, 2, 3, 5, 8, 13]


# -------------------------------------------------
# 3) Insert values into a dynamic array: 10, 20, 30, 40, 50
# -------------------------------------------------
print("\n3) Inserting values into dynamic array:")
arr = []
values_to_insert = [10, 20, 30, 40, 50]

for val in values_to_insert:
    arr.append(val)
    print(f"Inserted {val} → array now: {arr}")

print("Final array:", arr)


# -------------------------------------------------
# 4) Linear Search on array: [2, 5, 7, 10, 14, 20]
#    Target = 10 → should return index 3
#    Target = 9  → should return -1
# -------------------------------------------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("\n4) Linear Search:")
data = [2, 5, 7, 10, 14, 20]

target1 = 10
result1 = linear_search(data, target1)
print(f"Searching for {target1}: Found at index {result1}")

target2 = 9
result2 = linear_search(data, target2)
print(f"Searching for {target2}: Not found, returns {result2}")


# -------------------------------------------------
# 5) Binary Search (iterative) with full trace
#    Array: [11, 12, 20, 23, 40, 50] → sorted already
#    Target = 40 → should return index 4
# -------------------------------------------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    step = 0
    
    print(f"\n5) Binary Search Trace for target = {target}")
    print(f"Initial array: {arr}")
    print("-" * 50)
    
    while low <= high:
        step += 1
        mid = (low + high) // 2
        print(f"Step {step}: low={low}, high={high}, mid={mid}, arr[{mid}]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"Target {target} found at index {mid}!")
            return mid
        elif arr[mid] < target:
            print(f"{arr[mid]} < {target} → search right half")
            low = mid + 1
        else:
            print(f"{arr[mid]} > {target} → search left half")
            high = mid - 1
    
    print(f"Target {target} not found!")
    return -1

# Test binary search
sorted_arr = [11, 12, 20, 23, 40, 50]
binary_search(sorted_arr, 40)

# Extra: Time & Space Complexity
print("\nTime Complexity of Binary Search: O(log n)")
print("Space Complexity of Binary Search: O(1)")