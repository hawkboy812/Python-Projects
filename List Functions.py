#del - is only used in list and it is used to delete value using index number
#pop() - is similar to del it will delete the value as well as show the value that is deleted
#remove() - remove will del the value as it is without needing the index number
#clear() - clear is used to clear all the value

l=[20,30,40,50,60]
del l[1]
print(l)

print(l.pop(2))
print(l)

l=[20,30,40,50,60]
l.remove(60)
print(l)

l.clear()
print(l)

#update - update the value using index number
l=[20,30,40,50]
l[0]=90
print(l)

#insert() - it will add value without replacing the value will move forward.it will add the value as it is for ex if the value is nested
#append() - it will add value in front of other value/ insert can be used anywhere but append will add in front of the last value
#extends() - extend will put the value like append but extend it instead

l=[20,30,40,50]

l.insert(0,10)
print(l)

l=[20,30,40,50]
l.append(70)
print(l)

l=[20,30,40,50]
n=[70,80]
l.append(n)
print(l)

l=[20,30,40,50]
n=[70,80]
l.extend(n)
print(l)
