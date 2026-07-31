import random
import time

nums = list(range(1, 1_000_001))

# ---------------- Binary Search ----------------
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ---------------- Linear Search ----------------
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# Generate random targets
targets = [random.randint(1, 1_000_000) for _ in range(10)]


# -------- Linear Search Benchmark --------
start = time.perf_counter()

for target in targets:
    linear_search(nums, target)

linear_time = time.perf_counter() - start


# -------- Binary Search Benchmark --------
start = time.perf_counter()

for target in targets:
    binary_search(nums, target)

binary_time = time.perf_counter() - start


print(f"Linear Search Time : {linear_time:.6f} seconds")
print(f"Binary Search Time : {binary_time:.6f} seconds")
print("Target: ",targets)
print(f"\nBinary Search is approximately {linear_time / binary_time:.2f}x faster.")