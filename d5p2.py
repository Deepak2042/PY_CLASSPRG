grade=input("Enter the grade: ")
sal=float(input("Enter the salary: "))

bonus=0

if sal>0 and (grade=="A" or grade=="B"):
    if grade=='A':
        if sal<10000:
            bonus=(0.1*sal)+(0.02*sal)
        else:
            bonus=0.1*sal
    if grade=='B':
        if sal<10000:
            bonus=(0.1*sal)+(0.02*sal)
        else:
            bonus=0.1*sal

else:
    if sal<0:
        print("Salary can't be zero...!")
    if grade>="C" and grade<="Z":
        print("Grade doesn't exist...!!")

print("Salary: ",sal)
print("Bonus: ",bonus)
print("Total to be paid: ",bonus+sal)