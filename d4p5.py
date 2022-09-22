l1=[]
ele=int(input("Enter the no. of elements: "))
print("Enter the value: ")
for i in range(0,ele):
    val=int(input())
    l1.append(val)

f=0
count=0
try:
    while True:
        if count + l1[f] == len(l1):
            print(count)
            break
        if count + l1[f] == len(l1) - 1:
            print(count + 1)
            break
        if count + l1[f]+1== len(l1)-1:
            print(count + 2)
            break

        f += 1
        count += 1
except:
    print("End isn’t reachable...!")
