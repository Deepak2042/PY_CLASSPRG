val=int(input("Enter the value: "))
count=0
val1=0
val2=0
val3=0
cond=True
if val==1:
    count=1
else:
    while cond:
        for i in range(0, val):
            for j in range(0, val):
                for k in range(0, val):
                    if i ** 2 + j ** 2 + k ** 2 == val :
                        val1 = i
                        val2 = j
                        val3 = k
                        cond = False

if val1>0:
    count+=1
    if val2>0:
        count+=1
        if val3>0:
            count+=1

print(count)


