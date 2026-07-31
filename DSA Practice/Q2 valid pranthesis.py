s = input("Enter the string: ")

def valid(s):
    l=[]
    for i in s:
        if i in ["(","[","{"]:
            l.append(i)
        elif i in [")","]","}"]:
            if len(l)==0:
                return False
            if i==")":
                if "("==l[-1]:
                    l.pop()
                else:
                    return False
            elif i=="]":
                if "["==l[-1]:
                    l.pop()
                else:
                    return False
            elif i=="}":
                if "{"==l[-1]:
                    l.pop()
                else:
                    return False
    if len(l)==0:
        pass
    else:
        return False
    return True

print(valid(s))

def valid1(s):
    l=[]
    pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
    }
    for i in s:
        if i in pairs.values():
            l.append(i)
        elif i in pairs:
            if len(l)==0:
                return False
            if l[-1]==pairs.get(i):
                l.pop()
            else:
                return False
    if len(l)!=0:
        return False
    return True

print(valid1(s))