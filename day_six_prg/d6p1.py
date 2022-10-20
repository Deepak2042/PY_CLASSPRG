import math

l1=[]
check_val=0

def pythagorean_triplet(n):
    for b in range(n):
        for a in range(1, b):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0:
                add=[a,b,int(c)]
                l1.append(add)

try:
    lim = int(input("Enter the limit: "))
except:
    check_val=1

if check_val==0:
    if lim==0:
        print("Value can't be negative...!")
    elif lim<0:
        print("Value can't be negative...!")
    else:
        pythagorean_triplet(lim)
        for i in l1:
            print(tuple(i),end=" ")
else:
    print("Invalid input...!")