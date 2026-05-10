"""
Reads N, then N integers, then a query X. Prints the 1-based index of X
in the read sequence, or -1 if X was not among them.

OOP approach: data init / insertion / search are methods on NumberList.
"""


class NumberList:
    """Ordered collection of integers with 1-based index search."""

    def __init__(self) -> None:
        # Data initialization.
        self._numbers: list[int] = []

    def insert(self, value: int) -> None:
        """Append a value to the end of the collection."""
        self._numbers.append(value)

    def search(self, value: int) -> int:
        """Return the 1-based index of the first occurrence of value, or -1."""
        for i, v in enumerate(self._numbers, start=1):
            if v == value:
                return i
        return -1

    def __len__(self) -> int:
        return len(self._numbers)


def main() -> None:
    n = int(input())
    numbers = NumberList()
    for _ in range(n):
        numbers.insert(int(input()))
    x = int(input())
    print(numbers.search(x))


if __name__ == "__main__":
    main()
