tup = (1,2,3,5,6,4,"akhkfadkf",3,3,8,9)
c=tup.count(3)
print(c)
newtup = tup.__add__(tup)
print(newtup)



sett = {1,5,6,1,2,4,8,9,5,8,6,2,9,5,3,4,2,1}
print(sett)
sett.add("5")
#sett.clear() Makes it a empty set
csett = sett.copy()
csett.add("different element")
print(csett,":add")
print(csett.difference(sett),":difference")
#csett.difference_update() Update the set, removing elements found in others.
csett.discard(10)
print(csett.intersection(sett),":intersection")
#sett.intersection_update(csett) Update the set, keeping only elements found in it and all others.
print(csett.isdisjoint(sett),":isdisjoint")
print(csett.issubset(sett),":issubset")
#csett.pop()
sett.pop()
csett.pop() #removes elements from front FIFO
print(csett,":pop FIFO")
print(csett.issuperset(sett))
csett.remove(2) #If the element is not a member, raise a KeyError.
dsett = {"ASDFG",654,False}
print(csett.union(dsett))