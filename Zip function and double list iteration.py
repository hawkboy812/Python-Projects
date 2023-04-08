l=[10,20,40,50]
l1=[3,4,77,88,99]

#zip function is used to iterate multiple function at once.
# string index should be the same in both array or zip will ignore the index number that is not in the previous array
t=len(l)
for a,b in zip(l,l1):
    print(a,b)

#alternative way you can iterate is

for h in range(t):
    print(l[h],l1[h])