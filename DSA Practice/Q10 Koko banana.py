piles = [3,6,7,11]
h=int(input("Enter hours: "))
speed=int(input("Enter speed of Koko: "))

def canEat(piles, h, speed):
    count = 0
    for i in range(len(piles)):
        if piles[i] <= speed:
            count += 1
        elif piles[i] > speed:
            count = count + (piles[i]//speed) + (1 if piles[i]%speed>0 else 0)
        if count > h:
            return False
    return True

print(canEat(piles,h,speed))

def minspeed(piles, h):
    left = 1
    right = max(piles)
    answer = -1
    count = 0
    while left<=right:
        mid = (left+right)//2
        if canEat(piles,h,mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

def onefunct(piles,h):
    left = 1
    right = max(piles)
    answer = right
    while left<=right:
        mid = (left+right)//2
        count = 0

        for pile in piles:
            count += (pile + mid -1)//mid

            if count>h:
                break
        if count<=h:
            answer = mid
            right = mid -1
        else:
            left = mid + 1

    return answer

print(onefunct(piles,h),"Min speed")