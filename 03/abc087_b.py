# ABC087B - Coins

def main():
    # input
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    # compute
    """WRITE BELOW"""
    i = 0
    for a in range(0,A+1):
        for b in range(0,B+1):
            for c in range(0,C+1):
                if X == 500*a+100*b+50*c:
                    i += 1

    # output
    print(i)


if __name__ == '__main__':
    main()
