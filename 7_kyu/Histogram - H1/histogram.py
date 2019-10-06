"""
Histogram - H1
"""


def histogram(results):
    return ''.join([
        f'{i + 1}|{result*"#"}{" " + str(result) if result > 0 else ""}\n'
        for i, result in enumerate(results)
    ][::-1])
