import time 
nums = list(range(1, 1000000001))   

def bin_search(nums):
    left = 0
    right = len(nums) -1
    target = int(input("Enter num to search: "))
    stime = time.time()
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            etime = time.time()
            return f"Found at {mid} in {etime - stime} seconds"
        elif nums[mid] < target:
            left = mid + 1
            continue
        elif target < nums[mid]:
            right = mid -1
            continue
        
    return -1

print(bin_search(nums))




