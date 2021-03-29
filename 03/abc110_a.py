# ABC110A - Maximize the Formula

def main():
    # input
    numbers = list(map(int, input().split()))

    # compute
    """WRITE BELOW"""
    x = max(numbers)
    y = sorted(numbers)[-2]
    z = sorted(numbers)[-3]

    # output
    print(10*x+y+z)

if __name__ == '__main__':
    main()
