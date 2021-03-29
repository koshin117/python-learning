# ABC081B - Shift only

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    """WRITE BELOW"""
    flag = "True"
    x = -1
    while flag == "True":
        x += 1
        for i in range(0,N):
            if As[i] % 2 == 0:
                As[i] /= 2
            else:
                flag = "false"

    # output
    print(x)


if __name__ == '__main__':
    main()
