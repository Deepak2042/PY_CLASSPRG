l1=[]
num=[]
ele=int(input("Enter the total no. of values: "))
print("Enter the value: ")
for i in range(0,ele):
    val=int(input())
    num.append(val)



for i in range(0,ele):
    count=0
    for j in range(0,ele):
        if num[i]>num[j] and j!=i:
            count+=1
    l1.append(count)

print(l1)
