def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    # compute
    As.sort(reverse=True)
    A = 0
    B = 0
    for i in range(N):
        if i%2 == 0:
            A += As[i]
        else:
            B += As[i]
    # output
    print(A-B)

if __name__ == '__main__':
    main()
