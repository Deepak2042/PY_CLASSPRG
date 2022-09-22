#prg2
ns=0
tot_user=int(input("Enter the total user: "))
staff_user=int(input("Enter the staff user:"))
if tot_user==0 or staff_user==0:
    print("User Value can't be zero...!")
    exit()
elif tot_user<0 or staff_user<0:
    print("User Value can't be negative..")
    exit()

else:
    print("Total user: ",tot_user)
    print("Staff user: ",staff_user)

    ns=staff_user/3

    print("Student user: ",tot_user-staff_user-ns)
