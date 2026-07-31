s = "abcabcbb"

def substring_long(s):
    l = set()
    left = 0
    maxl = 0
    for right in range(len(s)):
        while s[right] in l:
            l.remove(s[left])
            left+=1
        l.add(s[right])
        current= right - left +1
        maxl=max(maxl,current)
        
    return maxl

print(substring_long(s))
