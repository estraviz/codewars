import pytest

from solution import oper_array, gcdi, lcmu, som, maxi, mini

arr1 = [18, 69, -90, -78, 65, 40]
arr2 = [10, 70, -97, -84, -96, -16]
arr3 = [-73, -79, 19, -15, 99, 84]
arr4 = [-41, 88, 72, 45, 46, 72]

data = [
    (gcdi, arr1, arr1[0], [18, 3, 3, 3, 1, 1]),
    (lcmu, arr1, arr1[0], [18, 414, 2070, 26910, 26910, 107640]),
    (som, arr1, 0, [18, 87, -3, -81, -16, 24]),
    (mini, arr1, arr1[0], [18, 18, -90, -90, -90, -90]),
    (maxi, arr1, arr1[0], [18, 69, 69, 69, 69, 69]),
    (gcdi, arr2, arr2[0], [10, 10, 1, 1, 1, 1]),
    (lcmu, arr2, arr2[0], [10, 70, 6790, 40740, 325920, 325920]),
    (som, arr2, 0, [10, 80, -17, -101, -197, -213]),
    (mini, arr2, arr2[0], [10, 10, -97, -97, -97, -97]),
    (maxi, arr2, arr2[0], [10, 70, 70, 70, 70, 70]),
    (gcdi, arr3, arr3[0], [73, 1, 1, 1, 1, 1]),
    (lcmu, arr3, arr3[0], [73, 5767, 109573, 1643595, 54238635, 1518681780]),
    (som, arr3, 0, [-73, -152, -133, -148, -49, 35]),
    (mini, arr3, arr3[0], [-73, -79, -79, -79, -79, -79]),
    (maxi, arr3, arr3[0], [-73, -73, 19, 19, 99, 99]),
    (gcdi, arr4, arr4[0], [41, 1, 1, 1, 1, 1]),
    (lcmu, arr4, arr4[0], [41, 3608, 32472, 162360, 3734280, 3734280]),
    (som, arr4, 0, [-41, 47, 119, 164, 210, 282]),
    (mini, arr4, arr4[0], [-41, -41, -41, -41, -41, -41]),
    (maxi, arr4, arr4[0], [-41, 88, 88, 88, 88, 88]),
]


@pytest.mark.parametrize("fct, arr, init, result", data)
def test_oper_array(fct, arr, init, result):
    assert oper_array(fct, arr, init) == result
