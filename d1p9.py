#prg9-

E=[]
L=[]
print("Enter the time value: ")
T = int(input())
if T<=0:
    print("Time can't negative or zero...!")
    exit()

print("Enter the entry values: ")
for i in range(T):
    e=int(input())
    E.append(e)
print("Enter the exit value: ")
for i in range(T):
    l=int(input())
    L.append(l)
Sum=0
Max=0
for i in range(T):
    Sum+=E[i]-L[i]
    Max=max(Sum,Max)
print("output", Max)