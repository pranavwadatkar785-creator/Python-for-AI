nums = [1,2,3,4]

def product_of_array(nums):
    product = 1
    l=[]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j:
                product = product * nums[j]
        l.append(product)
        product = 1
    return l

print(product_of_array(nums),"Brute Force O[n^2]")

def product_of_array_opt(nums):
    productl = 1
    productr = 1
    ans = [1]
    for i in range(1,len(nums)):
        productl = productl*nums[i-1]
        ans.append(productl)
    for i in range(len(nums)-1,-1,-1):
        ans[i] = ans[i] * productr
        productr = productr * nums[i]
    return ans
print(product_of_array_opt(nums))