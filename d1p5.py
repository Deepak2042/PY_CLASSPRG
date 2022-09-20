#prg5-

new_loaves=int(input("Enter the no. of new loaves purchased: "))
old_loaves=int(input("Enter the no. of old loaves purchased: "))
if new_loaves>0 and old_loaves>0:
    regular_price = 185
    print("Regular price: Rs.", regular_price)
    print("Amount of new loaves: Rs.", new_loaves * regular_price)
    discount = (60 * regular_price * old_loaves) / 100
    print("Amount of day old loaves: Rs.", discount)
    print("Total amount: Rs.", (new_loaves * regular_price) + discount)
else:
    print("Purchase can't be negative...!")