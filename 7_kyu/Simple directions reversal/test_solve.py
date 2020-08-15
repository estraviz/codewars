from solve import solve


def test_solve():
    arr = ['Begin on 3rd Blvd', 'Right on First Road', 'Left on 9th Dr']
    rev = ['Begin on 9th Dr', 'Right on First Road', 'Left on 3rd Blvd']
    assert solve(arr) == rev

    arr = ["Begin on Road A", "Right on Road B", "Right on Road C",
           "Left on Road D"]
    rev = ['Begin on Road D', 'Right on Road C', 'Left on Road B',
           'Left on Road A']
    assert solve(arr) == rev

    arr = ["Begin on Road A"]
    rev = ["Begin on Road A"]
    assert solve(arr) == rev
