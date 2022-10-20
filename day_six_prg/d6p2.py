check_point=1
fact=1

try:
    val=int(input("Enter the value: "))
except:
    check_point=0

if check_point==1:
    if val>0:
        while val>0:
            fact *= val
            val -= 1
        print("Factorial: ",fact)

    elif val==1 or val==0:
        fact=val
        print("Factorial: ",fact)


    elif val<0:
        while val<0:
            fact*=val
            val+=1
        print("Factorial: ",-1*fact)
else:
    print("Invalid input...!")
