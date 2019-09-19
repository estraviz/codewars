from covfefe import covfefe


def test_covfefe():
    assert covfefe("coverage") == "covfefe"
    assert covfefe("coverage coverage") == "covfefe covfefe"
    assert covfefe("nothing") == "nothing covfefe"
    assert covfefe("double space ") == "double space  covfefe"
    assert covfefe("covfefe") == "covfefe covfefe"
