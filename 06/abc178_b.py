def main():
    # input
    a,b,c,d = map(int,input().split())
    # compute

    # output
    print(max(a*c,a*d,b*c,b*d))

if __name__ == '__main__':
    main()
