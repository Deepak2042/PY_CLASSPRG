check_val=0
try:
    ran = int(input("Enter the limit: "))
except:
    check_val=1

if check_val==1:
    print("Invalid input...")
else:
    if ran==0:
        print("Enter value greater than Zero...!")
    elif ran<0:
        print("Value can't be negative..")
    else:
        for i in range(ran + 1):
            num = 0.1
            for j in range(i):
                print(round(num, 2), end=" ")
                num = num + 0.1
            print("\r")
