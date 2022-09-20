#prg6-

def min(value1,value2):
    if(value1 < value2):
        return value1
    else:
        return value2


list=[]
count=int(input("total no. of values going to enter: "))
print("Enter the value: ")
for i in range(0,count):
    val=int(input())
    list.append(val)

max=0
for ele in list:
    if ele>max:
        max=ele
# print(max)
dis=0
i=list.index(max)
# print(i)
max_index=0
for el in list:
    if i>list.index(el):
        if i-list.index(el) > max_index:
            max_index = (list.index(el) + 1) - (i + 1)
    else:
        if list.index(el)-i > max_index:
            max_index = (list.index(el) + 1) - (i + 1)
# print(max_index)
# print(list[max_index])
dis=i+max_index
ret_val=min(list[i],list[max_index])
print("max: ",ret_val)