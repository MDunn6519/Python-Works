"""
memoization is the top- down approach to things.
more efficient recursion method.
"""


def fib_memoization(n: int, lookup: dict) -> int:
    if n < 1:
        return -1
    if n == 1 | n == 2:
        lookup[n] = 1
    if lookup.get(n, None) is None:
        lookup[n] = fib_memoization(n-1, lookup) + fib_memoization(n-2, lookup)
    return lookup[n]


"""
Tabulation is the bottom-up approach to recursion   
more efficient. uses iteration
"""


def fib_tab(n: int) -> int:
    f = [0] * (n+1)
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


def main() -> int:
    my_diction = {}

    f = fib_memoization(6, my_diction)
    print(f)


if __name__ == '__main__':
    main()