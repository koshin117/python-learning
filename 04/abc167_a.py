S = input()
T = input()
count = 0
if S+"0" <= T:
    count += 1
if S+"z" >= T:
    count += 1
if count == 2:
    print("Yes")
else:
    print("No")
