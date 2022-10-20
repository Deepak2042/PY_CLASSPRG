A=int(input("Enter the limit_A: "))
B=int(input("Enter the limit_B: "))
str=[]
if A<B:
    for i in range(A+1,B,1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count=count+1
        if count>2:
            str.append(i)
    print(str)
elif A>B:
    for i in range(A,B,-1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count=count+1
        if count>2:
            str.append(i)
    print(str)

elif A==B:
    print("Both the limits are same..!")