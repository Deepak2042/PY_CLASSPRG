n=int(input("Enter the total element: "))

l1=[]
sum=0
for i in range(n):
    val=float(input())
    l1.append(val)
    sum=sum+val

mean=sum/n
print("Mean: ",mean)

counter=[]
for i in l1:
    counter.append(l1.count(i))
max=0
pos=0
for i in range(len(counter)):
    if counter[i]>max:
        max=counter[i]
        pos=i
l1.sort()
res=0
if n%2==0:
    val1=n/2
    val2=(n/2)+1
    res=l1[int(val1)]+l1[int(val2)]
    print("Median: ",res)
elif n%2!=0:
    val3=int(n/2)
    res=l1[val3]
    print("Median: ",res)

print("Mode: ",l1[pos])
