# n=int(input("Enter the n value: "))
# m=int(input("Enter the M value: "))
#
# l1=[]
# val=6
# sum=0
#
#
# # while n>0:
# #
# #     for i in range(1,val+1,1):
# #         if val%i==0:
# #             sum=sum+i
# #     if sum==val:
# #         l1.append(val)
# #         n=n-1
# #     val=val+1
# #     sum = 0
# #
# # print(l1)
# l1=[]
# def isPerfect(num):
#     for i in range(1, num):
#         sum_v = 0
#         if num % i == 0:
#             sum_v = sum_v + i
#
#         if sum_v==num:
#             l1.append(num)
#             print(sum_v,end=" ")
#             return True
#         else:
#             return False
#
# # N, M = [int(i) for i in input().split(" ")]
# N=int(input())
# M=int(input())
# i=0
# num=6
#
# while(i<N):
#     if (isPerfect(num))==True:
#         i+=1
#         num+=1
#         isPerfect(num)
#     else:
#         num+=1
#         isPerfect(num)
#
# print(l1)

l1=[]

def isPerfect(lim):
    num=6
    while lim>0:
        sum = 0
        for i in range(1,num):
            if num % i == 0:
                sum += i
        if sum == num:
            # print(num)
            l1.append(num)
            lim-=1
        num+=1
    print(l1)


def isFactor():
    for i in l1:
        count = 0
        print(i,end="-")
        for j in range(1,i+1,1):
            if i%j==0 and count<=M:
                print(j,end=",")
                count+=1
            else:
                break
        print("\n")

N=int(input())
M=int(input())

isPerfect(N)
isFactor()

