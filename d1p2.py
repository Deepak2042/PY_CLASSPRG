#prg2-
def sumsquare(l1):
    odd_sum=0
    eve_sum=0
    for num in l1:
        if num%2==0:

            eve_sum+=num**2
        else:
            odd_sum+=num**2

    print("Sum of all odd values: ",odd_sum)
    print("Sum of all even values: ",eve_sum)

list1=[]
count=int(input("Enter the no. of elements: "))
if(count<=0):
    print("Input can't be ZERO...!")
else:
    print("Enter the value: ")
    for i in range(0,count):
        val=int(input())
        list1.append(val)

    sumsquare(list1)
