#prg10-

str=input("Enter the value: ")
new_str=''
list=[]
for i in range(0,len(str)):
    list.append(str.count(str[i]))
    new_val=ord(str[i])
    print(chr(new_val+list[i]),end="")