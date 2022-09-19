# prg1-

# s=input("Enter the String one: ")
# t=input("Enter the String two: ")
#
# if len(s)==len(t):
#     print("true")
# else:
#     print("false")

#prg2-

# def sumsquare(l1):
#     odd_sum=0
#     eve_sum=0
#     for num in l1:
#         if num%2==0:
#
#             eve_sum+=num**2
#         else:
#             odd_sum+=num**2
#
#     print("Sum of all odd values: ",odd_sum)
#     print("Sum of all even values: ",eve_sum)
#
# list1=[]
# count=int(input("Enter the no. of elements: "))
# if(count<=0):
#     print("Input can't be ZERO...!")
# else:
#     print("Enter the value: ")
#     for i in range(0,count):
#         val=int(input())
#         list1.append(val)
#
#     sumsquare(list1)

#prg3-
#
# def checkone(num):
#     sum=0
#     while num>=1:
#         rem = num % 10
#         sum+= int(rem*rem)
#         num=int(num/ 10)
#
#     if sum == 1:
#         print("True")
#     else:
#         checkone(sum)
#
# val = int( input ("Enter the value: "))
# checkone(val)

#prg-4

# val=input("Enter the value: ")
# val1=val[::-1]
# if(val==val1):
#     print("Palindrome")
# else:
#     print("Not palindrome")

#prg-5

# new_loaves=int(input("Enter the no. of new loaves purchased: "))
# old_loaves=int(input("Enter the no. of old loaves purchased: "))
# if new_loaves>0 and old_loaves>0:
#     regular_price = 185
#     print("Regular price: Rs.", regular_price)
#     print("Amount of new loaves: Rs.", new_loaves * regular_price)
#     discount = (60 * regular_price * old_loaves) / 100
#     print("Amount of day old loaves: Rs.", discount)
#     print("Total amount: Rs.", (new_loaves * regular_price) + discount)
# else:
#     print("Purchase can't be negative...!")

#prg-6
#
# def min(value1,value2):
#     if(value1 < value2):
#         return value1
#     else:
#         return value2
#
#
# list=[]
# count=int(input("total no. of values going to enter: "))
# print("Enter the value: ")
# for i in range(0,count):
#     val=int(input())
#     list.append(val)
#
# max=0
# for ele in list:
#     if ele>max:
#         max=ele
# print(max)
# dis=0
# i=list.index(max)
# print(i)
# max_index=0
# for el in list:
#     if i>list.index(el):
#         if i-list.index(el) > max_index:
#             max_index = (list.index(el) + 1) - (i + 1)
#     else:
#         if list.index(el)-i > max_index:
#             max_index = (list.index(el) + 1) - (i + 1)
# print(max_index)
# print(list[max_index])
# dis=i+max_index
# ret_val=min(list[i],list[max_index])
# print("max: ",ret_val*dis)

#prg7-
# def countstrings(n, start):
#     if n == 0:
#         return 1
#     cnt = 0
#     for i in range(start, 5):
#         cnt += countstrings(n - 1, i)
#     return cnt
#
#
# def countVowelStrings(n):
#     return countstrings(n, 0)
#
#
# val=int(input("Enter the number of string"))
# if(val>0):
#     print(countVowelStrings(val))
# else:
#     print("Value can't be zero...!")

#prg8-
# def isNumeric(s):
#    s = s.strip()
#    try:
#       s = float(s)
#       return True
#    except:
#       return False
#
# str=input("Enter the value: ")
# ret_val=isNumeric(str)
# print(ret_val)


#prg9-

# E=[]
# L=[]
# print("Enter the time value: ")
# T = int(input())
# print("Enter the entry values: ")
# for i in range(T):
#     e=int(input())
#     E.append(e)
# print("Enter the exit value: ")
# for i in range(T):
#     l=int(input())
#     L.append(l)
# Sum=0
# Max=0
# for i in range(T):
#     Sum+=E[i]-L[i]
#     Max=max(Sum,Max)
# print("output", Max)

#prg10-
# str=input("Enter the value: ")
# new_str=''
# list=[]
# for i in range(0,len(str)):
#     list.append(str.count(str[i]))
#     new_val=ord(str[i])
#     print(chr(new_val+list[i]),end="")

