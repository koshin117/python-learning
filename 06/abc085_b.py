def main():
    # input
    N = int(input())
    Ds = [int(input()) for _ in range(N)]
    # compute
    Ds.sort(reverse=True)
    count = 0
    for i in range(N-1):
        if Ds[i] == Ds[i+1]:
            count += 1
    print(N-count)

    # output

if __name__ == '__main__':
    main()
