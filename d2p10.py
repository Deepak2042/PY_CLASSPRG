s1=input("Enter the string-1 value: ")
s2=input("Enter the string-2 value: ")
l1=[]

for i in range(0,len(s1)):
    list1=list(s1.split())
for i in range(0,len(s2)):
    list2=list(s2.split())

max_len=0
if len(list1)<len(list2):
    max_len=len(list1)
else:
    max_len=len(list2)

for i in range(0,max_len):
    if list1[i] in list2:
        l1.append(list1[i])
print(l1)