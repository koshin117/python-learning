#E
def gcd(As :int) -> int:
    N = As[0]
    M = As[1]
    if N == M:
        return N
    elif N > M:
        N %= M
        if N == 0:
            return M
        else:
            As[0] = N
            return gcd(As)
    else:
        As[0],As[1] = M,N
        return gcd(As)
def main():
    # input
    As = list(map(int, input().split()))
    # compute

    # output
    print(gcd(As))

if __name__ == '__main__':
    main()
