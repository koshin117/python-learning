def main():
    # input
    Ss = list(input())

    # compute
    As = []
    for i in range(0,len(Ss)):
        if i%2 == 0:
            As += Ss[i]

    # output
    print("".join(As))

if __name__ == '__main__':
    main()
