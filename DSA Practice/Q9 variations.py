array = [False, False, False, False, True, True, True]

def boundary_search(array):
    left = 0
    right = len(array)-1
    ans = -1
    while left<=right:
        mid = (left + right)//2
        if array[mid]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


print(boundary_search(array))