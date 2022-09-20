
s=input("Enter the String one: ")
t=input("Enter the String two: ")
if len(s) != len(t):
    print("Flase")
    quit()
max_len=0
count1=0

if(len(s)==len(t)):
    max_len=len(s)
elif(len(s)<len(t)):
    max_len=len(s)
elif(len(s)>len(t)):
    max_len=len(t)

for i in range(0,max_len-1):
    if s[i]==s[i+1]:
        count1+=1
    if t[i]==t[i+1]:
        count1+=1

if count1==0 or count1==2:
    print("True")
else:
    print("False")


