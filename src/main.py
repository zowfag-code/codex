"""Example entry point for the project."""

from src.math_utils import add, is_even


def main() -> None:
    result = add(2, 3)
    print(f"2 + 3 = {result}")
    print(f"Is {result} even? {is_even(result)}")


if __name__ == "__main__":
    main()
