"""Complete The Pattern #7 - Cyclical Permutation"""


def pattern(n):
    nums = [str(i) for i in list(range(1, n+1))]
    output = []
    for i in range(len(nums)):
        output.append("".join(nums))
        nums = list(nums[1:]) + [nums[0]]
    return "\n".join(output)
