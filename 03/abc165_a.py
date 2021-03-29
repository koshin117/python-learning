# ABC165A - We Love Golf

def main():
    # input
    K = int(input())
    A, B = map(int, input().split())

    # compute
    """WRITE BELOW"""
    x = 0
    while x < A:
        x += K

    # output
    if x <= B:
        print("OK")
    else:
        print("NG")


if __name__ == '__main__':
    main()
