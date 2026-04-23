from __future__ import annotations

from typing import Union


def x(a: Union[int, float, str], b: Union[int, float, str], c: int) -> float:
    """Calculate a percentage of the sum of a and b.

    - c == 1: return 18% of the sum
    - c == 2: return 10% of the sum
    - otherwise: raise a clear error
    """
    try:
        d = float(a) + float(b)
    except (TypeError, ValueError) as exc:
        raise TypeError("a and b must be numeric values") from exc

    if c == 1:
        return d * 0.18
    elif c == 2:
        return d * 0.10
    else:
        raise ValueError("c must be 1 or 2")


if __name__ == "__main__":
    print(x(100, 50, 1))
    print(x(200, "50", 2))
    try:
        print(x(10, 20, 3))
    except ValueError as exc:
        print(f"Error: {exc}")
