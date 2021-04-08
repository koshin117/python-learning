def main():
    # input
    N,A,B = map(int,input().split())
    # compute
    Ssum = 0
    for i in range(1,N+1):
        a = i
        sum = 0
        while i>0:
            sum += i%10
            i = i // 10
        if A <= sum and sum <= B:
            Ssum += a
    # output
    print(Ssum)

if __name__ == '__main__':
    main()
