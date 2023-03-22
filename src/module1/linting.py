import math
import random


def main(
    a: int,
    b: int,
    c: int,
    d: int,  # pylint: disable=unused-argument
    unused_var_e: float,
    unused_var_f: float,
    unused_var_g: float,  # pylint: disable=unused-argument
) -> None:
    """Sum and print the input integers.

    Args:
        a (int): arg 1
        b (int): arg 2
        c (int): arg 3
        d (int): arg 4
    """
    my_list = ["apple", "banana", "cucumber", "mango"]
    print("running main")

    print(math.pi)
    print(my_list[0:2])
    print(f"a + b + c = {a+b+c}")


if __name__ == "__main__":
    main(2, 3, 4)
    print(random.uniform())

    print()
