l1=[]
ele=int(input("Enter the no. of elements: "))

print("Enter the elements: ")
for i in range(0,ele):
    val=int(input())
    l1.append(val)

count=0

for i in range(0,ele-1):
    if l1[i]<l1[i+1]:
        count=l1[i]

print("Peak: ",count)

