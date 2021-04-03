from typing import NoReturn


def bubble_sort(N :list) -> list:
    x = len(N)
    while x != 1:
        for i in range(x-1):
            if N[i] > N[i+1]:
                N[i], N[i+1] = N[i+1], N[i]
        x -= 1
    return N
def main():
    # input
    N = list(map(int, input().split()))
    # compute


    # output
    print(bubble_sort(N))

if __name__ == '__main__':
    main()
