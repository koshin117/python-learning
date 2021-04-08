def main():
    # input
    N = int(input())
    As = list(map(int,input().split()))
    # compute
    As = sorted(As)
    if N == 1:
        print(1)
    else:
        Cs = [0 for _ in range(N)]
        for i in range (0,N):
            for j in range(i,N):
                if As[j] <= As[i]+2:
                    Cs[i] += 1
                else:
                    break
        print(max(Cs))
    # output


if __name__ == '__main__':
    main()
