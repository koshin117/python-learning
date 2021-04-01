N = int(input())
count = 0
if N//100 == 7:
    count += 1
N %= 100
if N//10 == 7:
    count += 1
if N%10 == 7:
    count += 1
if count != 0:
    print("Yes")
else:
    print("No")
