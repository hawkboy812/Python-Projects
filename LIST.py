#list is mutable or value is changeable
#[] to define list u can take integer string or list inside list
#list is , comma seprated
#list contain multiple valuue for ex alphabets and numericals nested list etcc
l=[1,2,3,4,5]
print(type(l))
#nested list is square backet inside sqquare bracket for ex 4,5,6 is nested = get 5 inside the nested bracket
l=[1,2,3,[4,5,6]]
print(l[3][1])
#mixedd list contains nested list nnumbers and alpabets
l=[2,3,'hello',[3,4,5]]
print(l[2])
#mixed slicing is same as string slicing
print(l[0:2])
# asnwer will come in list as well as 0:2 it will start from 0 and the condition is index number 2 in this case
print(l[1:])
l=[1,2,3,4,5,6]
#increment is 2 in this case and blank space is condition(no condition in this case) 0 is defined as the starting index point
print(l[0: :2])
#reverse slice
print(l[-1: :-1])
#multiple value
l=[10,20,30,40,'hello']
print(l[3],l[4])