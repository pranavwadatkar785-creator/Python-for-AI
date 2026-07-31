nums = [1,3,4,2,]

def contains_duplicate(nums):
    l = len(nums)
    for i in range(l):
        for j in range(i+1,l):
            if nums[i] == nums[j]:
                return True
    return False
print(contains_duplicate(nums),"Brute Force.")

def optimal(nums):
    l=len(nums)
    d={}
    for i in range(l):
        if nums[i] in d:
            return True
        d[nums[i]]=nums[i]
    return False
    
print(optimal(nums),"Optimal using Hash Map.")

def optimal_set(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

print(optimal_set(nums),"Optimal using Hash Set.")