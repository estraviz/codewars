def sum_of_differences(arr):
    arr.sort(reverse=True)
    return sum(x - y for x, y in zip(arr, arr[1:]))
