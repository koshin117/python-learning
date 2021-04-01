def main():
    # input
    N = input()
    # compute
    As = list(map(int, N))
    x = sum(As)
    # output
    if x % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
