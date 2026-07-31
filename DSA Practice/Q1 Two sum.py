nums = [2,5,3,4,11,12,6,7,15,16,13]
targett = int(input("Enter Num: "))
def two_sum1(nums,targett):
    lenn=len(nums)
    for i in range(lenn):
        for j in range(i+1,lenn): 
            if nums[i] + nums[j]==targett:
                return [i,j]
    return "No such numbers"
print(two_sum1(nums,targett),"Time complexity O[n^2]")

nums = [2,5,3,4,11,12,6,7,15,16,13]
def two_sum2(nums,targett):
    lenn=len(nums)
    d={}
    for i in range(lenn):
        j = targett - nums[i]
        if j in d:
            return [i,d.get(j)]
        d[nums[i]] = i
    return []

print(two_sum2(nums,targett),"Time complexity O[n]")
