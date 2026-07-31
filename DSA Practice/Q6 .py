nums = [4,-1,2,1,-10]

def max_subarray(nums):
    max_subarray = [nums[0]]
    max_num = nums[0]
    for i in range(len(nums)):
        summ = 0
        check_array = []
        for j in range(i,len(nums)):
            summ = summ + nums[j]
            check_array.append(nums[j])
            if summ > max_num:
                max_num = summ
                max_subarray.clear()
                max_subarray.extend(check_array)
    return max_subarray,max_num

print(max_subarray(nums),"Brute Force")

def opt_maxsubarray(nums):
    max_sum = nums[0]
    summ = 0
    for i in range(len(nums)):
        summ = summ + nums[i]
        if summ > max_sum:
            max_sum = summ
        if summ < 0:
            summ = 0
    return max_sum

print(opt_maxsubarray(nums),"Optimized")