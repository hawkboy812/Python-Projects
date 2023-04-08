#list comprehension elegant way to define and create list based on existing list
#list comprehension is generally more compact and faster than normal functions and loops for creating lists

#[expression for item in list]
l=[]
for a in range(1,101,1):
 l.append(a)

print(l)

n=[h for h in range(1,101) if h%2==0]
print(n)

s='hello'
d=[g for g in s]
print(d)