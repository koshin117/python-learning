def main():
    # input
    N,D = map(int, input().split())
    Ass = [list(map(int, input().split())) for _ in range(N)]
    # compute
    count = 0
    for i in range(N):
        if ((Ass[i][0]**2)+(Ass[i][1]**2))**0.5 <= D:
            count += 1
    # output
    print(count)

if __name__ == '__main__':
    main()
