"""Prefill an Array"""


def prefill(n, v="undefined"):
    try:
        if (n := int(n)) == 0:
            return []
        return [v] * n
    except (TypeError, ValueError):
        return f"{n} is invalid"
