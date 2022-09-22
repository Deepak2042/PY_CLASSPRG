# val1=input("Enter the value_1: ")
# val2=input("Enter the value_2: ")
#
# max_len=0
# if len(val1)>len(val2):
#     max_len=len(val1)
# else:
#     max_len=len(val2)
#
# #print(bin(int(val1)+int(val2)))
# bin_val=n=bin(int(val1)+int(val2))
# print(bin_val)
# l1=list(bin_val.split())
# str=l1[0]
# for i in range(max_len+1,len(str)):
#     print(str[i],end='')


# Python program to add two binary numbers.

try:
    a = input("Enter the 1st binary value: ")
    b = input("Enter the 2nd binary value: ")

    sum = bin(int(a, 2) + int(b, 2))

    print(sum[2:])
except:
    print("Invalid input...!")