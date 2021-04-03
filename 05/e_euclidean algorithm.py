def gcd(N,M :int) -> int:
    if N == M:
        return N
    elif N > M:
        N %= M
        if N == 0:
            return M
        else:
            return gcd(M,N)
    else:
        return gcd(M,N)
def main():
    # input
    N, M = map(int, input().split())
    # compute

    # output
    print(gcd(N,M))

if __name__ == '__main__':
    main()
