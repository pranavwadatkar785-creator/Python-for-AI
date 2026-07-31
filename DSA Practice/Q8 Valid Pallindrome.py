s = "A man, a plan, a canal: Panama"

def check(s):
    ns=s.lower()
    l = []
    nl = []
    for i in range(len(ns)):
        if ns[i].isalnum():
            l.append(ns[i])
    nl.extend(l)
    l.reverse()
    if l == nl:
        return True
    return False

print(check(s),"Time: O(n), Space: O(n)")

def check_opt(s):
    ns = s.lower().strip()
    left = 0
    right = len(ns) - 1
    while left < right:
        if ns[left].isalnum() and ns[right].isalnum():
            if ns[left] == ns[right]:
                left += 1
                right -= 1
            else:
                return False
        else:
            if not ns[left].isalnum():
                left += 1
                continue
            if not ns[right].isalnum():
                right -= 1
                continue
    return True

print(check_opt(s),"Time: O(n), Space: O(1)")