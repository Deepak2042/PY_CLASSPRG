l1=[]

val=int(input("Enter the value: "))

for i in range(1,val+1):
    if i%3==0 and i%5==0:
        l1.append("FizzBuzz")
    elif i%5==0:
        l1.append("Buzz")
    elif i%3==0:
        l1.append("Fizz")
    else:
        l1.append(i)
print("Sequence: ",end="\n")
print(l1)
    
