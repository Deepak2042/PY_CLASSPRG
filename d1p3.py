#prg3-

def checkone(num):
    try:
        sum = 0
        while num >= 1:
            rem = num % 10
            sum += int(rem * rem)
            num = int(num / 10)

        if sum == 1:
            print("True")
        else:
            checkone(sum)
    except:
        print("False")


val = int( input ("Enter the value: "))
if val==2 or val==4:
    print("False")
    exit()
if val<=0:
    print("Flase")
    exit()
checkone(val)