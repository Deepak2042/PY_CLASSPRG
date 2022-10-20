num=float(input("Enter the value: "))
ran=int(input("Enter the limit: "))

if num<=0 :
    print("Value can't be Zero or negative...!")
elif ran<=0:
    print("Range can't be Zero or Negative...!")
else:
    ran = ran + 1
    for i in range(ran):
        for j in range(i):
            print(round(num, 2), end=" ")
            num = num + 0.1
        print("\r")
