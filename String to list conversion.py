
n=input("Enter the value")

print(n)
#split() function will breakdown a value and convert it to a list
l=n.split()

print(l)

l=[]
for a in range(1,4):
    n=input("Enter the value:-"+str(a)+":-")
    l.append(n)
    print(l)