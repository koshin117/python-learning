def main():
    # input
    X,t = map(int,input().split())
    # compute
    a = X - t

    # output
    if a >= 0:
        print(a)
    else:
        print(0)

if __name__ == '__main__':
    main()
