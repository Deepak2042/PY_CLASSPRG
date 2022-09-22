l1=[]
ele=int(input("Enter the no. of elements: "))
print("Enter the value: ")
for i in range(0,ele):
    val=int(input())
    l1.append(val)
count=0
for i in range(0,ele):
    for j in range(0,ele):
        if ((l1[i]==l1[j]) and (i<j)):
            # print("(",i,",",j,")",end=',')
            count+=1

print("Good pairs: ",count)