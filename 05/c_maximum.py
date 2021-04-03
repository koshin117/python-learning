#C
def my_max(As :list) -> int:
    return max(As)
def main():
    # input
    As = list(map(int, input().split()))
    # compute

    # output
    print(my_max(As))
if __name__ == '__main__':
    main()
