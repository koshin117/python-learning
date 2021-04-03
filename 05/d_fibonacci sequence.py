#D
def fibonacci(N :int) -> int:
    if N == 1:
        return 1
    elif N == 2:
        return 1
    else:
        return fibonacci(N-2)+fibonacci(N-1)
def main():
    # input
    N = int(input())
    # compute

    # output
    print(fibonacci(N))
if __name__ == '__main__':
    main()
