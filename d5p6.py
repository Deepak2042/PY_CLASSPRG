import math
# nCr = n!/((n-r)!*r!)

def fact(n,r):
    ret=math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    return ret

rows=int(input("Enter the number of rows: "))
row=int(input("Enter the row number: "))

sum=0

if rows<0 or row<0:
    if rows<0:
        print("Rows can't be zero...!")
    if row<0:
        print("Row can't be zero...!")
else:
    for i in range(rows + 1):
        for k in range(i + 1):
            val = fact(i, k)
            if i == row - 1:
                sum += int(val)
                
    print(sum)