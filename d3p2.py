l1=[]
value=input("Enter the value: ")
if int(value)<0:
    print("Value  can't be negative...!")
    exit()
if len(value)>3:
    print("Not an three digit value...!")
    exit()

for i in range(0,3):
    val=int(value[i])
    l1.append(val)
if l1[0]==l1[1] and l1[1]==l1[2]:
    print("Combination: ")
    print(l1)
    exit()
print("Combination: ")

for i in range(0,3):
   for j in range(0,3):
      for k in range(0,3):
         if i!=j & j!=k & k!=i:
            print(l1[i],l1[j],l1[k])