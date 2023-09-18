l=[1,2,3,4,5]
l2=[]
a=0
print("First list:",l)
for i in range(0,5):
    l[i]=l[i]**2
    l2.append(l[i])
    a=a+l[i]
print("Second list:",l2)
print("Sum of all new values:",a)