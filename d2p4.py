l1=[]
l2=[]

lim1=int(input("Enter the no. of elements in list1: "))
lim2=int(input("Enter the no. of element in list2: "))

print("Enter the list_1 elements: ")
for i in range(0,lim1):
     val=int(input())
     l1.append(val)

print("Enter the list_2 elements: ")
for i in range(0,lim2):
     val=int(input())
     l2.append(val)

l3=l1+l2
print(sorted(l3))

