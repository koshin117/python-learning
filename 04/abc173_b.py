def main():
    # input
    N = int(input())
    Ss = [input() for _ in range(N)]
    # compute
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(N):
        if Ss[i] == "AC":
            ac += 1
        elif Ss[i] == "WA":
            wa += 1
        elif Ss[i] == "TLE":
            tle += 1
        else:
            re += 1
    # output
    print("AC x",ac)
    print("WA x",wa)
    print("TLE x",tle)
    print("RE x",re)

if __name__ == '__main__':
    main()
