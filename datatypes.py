a=5
print(a,type(a))
a=5.5
print(a,type(a))
a=2+5j
print(a,type(a))


s="hello@123"
print(s,type(s))
s='''hello
welcome to esports
'''
print(s)

s='10'
print(s,type(s))
l=[10,'ws',5.5]
l[2]=10
#list is muttable and string is immutable
print(l,type(l))
#tuple is immuttable but faster than list both are similar it is defined with ()
t=(10,20,'hello')
print(t,type(t))
t=(10)#only more than one value will count as tuple or it will be integer(datatype of the singular valuez)
print(t,type(t))
d={
    'course_name':'python',
    'course_duration': "2 month"
}
print(d,type(d))
#set is immutable it is defined with {}
s={10,20,30,10}
print(s,type(s))