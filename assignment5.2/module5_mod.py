"""Class module: ordered integer collection with 1-based index search."""


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