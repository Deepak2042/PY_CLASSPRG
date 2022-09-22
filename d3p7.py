from itertools import permutations
l1=[]
l2=[]
ele=int(input("Enter the no. of values: "))
print("Enter the vales: ")
for i in range(0,ele):
    val=int(input())
    l1.append(val)

perm=permutations(l1)
for i in list(perm):
    l2.append(i)
l2=list(set(l2))
print(l2)
