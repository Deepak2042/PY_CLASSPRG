str=input("Enter the expression: ")
sum=0
for i in range(0,len(str)-1):
    if str[i].isdigit()==True:
        sum+=int(str[i])
    if str[i]=='*':
        sum*=int(str[i+1])
    if str[i]=='+':
        sum+=int(str[i+1])
    if str[i]=='-':
        sum-=int(str[i+1])
    if str[i]=='/':
        sum/=int(str[i+1])


print(int(sum))
