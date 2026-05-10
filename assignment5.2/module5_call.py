"""
Main program: reads N, then N integers, then a query X. Prints the
1-based index of X in the read sequence, or -1 if X was not among them.

Uses NumberList from module5_mod.
"""

from module5_mod import NumberList


def main() -> None:
    n = int(input())
    numbers = NumberList()
    for _ in range(n):
        numbers.insert(int(input()))
    x = int(input())
    print(numbers.search(x))


if __name__ == "__main__":
    main()