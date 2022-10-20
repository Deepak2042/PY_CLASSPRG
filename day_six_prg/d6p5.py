def triangle(n):

    k = n - 1

    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")

        k = k - 1

        for j in range(i, 0,-1):
            print(j, end=" ")
        print("\r")

check_val=0
try:
    n = int(input("Enter the limit: "))
except:
    check_val=1

if check_val==1:
    print("Invalid input...")
else:
    if n==0:
        print("Enter value greater than Zero...!")
    elif n<0:
        print("Value can't be negative..")
    else:
        triangle(n+1)





