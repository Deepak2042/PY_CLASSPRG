#prg4
s=input("Enter the phrase: ")
str="" 
for i in s:
    if i>='A' and i<='Z' or i>='a' and i<='z' :
        str+=i
str=str.lower()
#print(str)
if str==str[::-1]:
    print(True)
else:
    print(False)
#print(str)

