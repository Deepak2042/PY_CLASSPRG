def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


N = int(input())
arr = [int(i) for i in input().split(" ")]

LCM = compute_lcm(arr[0], arr[1])
GCD = arr[0]*arr[1] / LCM
for i in range (2, N):
    GCD = arr[i] * LCM
    LCM = compute_lcm(LCM, arr[i])
    GCD = GCD / LCM

print(LCM, int(GCD))