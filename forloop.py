#range(5)
#start=0
#condition<5
#increment 1
#0 1 2 3 4
#range(1,6)
#start=1
#condition<6
#increment 1
# 1 2 3 4 5
#range(1,6,2)
#start=1
#condition<6
#increment 2
#1 3 5

for n in range(5):
    print(n)

for n in range(1,6):
    print(n)

for n in range(1,6,2):
    print(n)

for a in range(1,11):
    print("2*",a,"=",2*a)
#range(10,0,-1) Decrement by -1 reverse case
for n in range(10,-1,-2):
    print(n)