"""Prefill an Array"""


def prefill(n, v="undefined"):
    try:
        return [v] * int(n)
    except (TypeError, ValueError):
        return f"{n} is invalid"
