from generate_link import generate_link


def gen_test_case(inp, res):
    assert generate_link(inp) == res


def test_generate_link():
    gen_test_case('matt c', 'http://www.codewars.com/users/matt%20c')
    gen_test_case('g964', 'http://www.codewars.com/users/g964')
    gen_test_case('GiacomoSorbi', 'http://www.codewars.com/users/GiacomoSorbi')
    gen_test_case('ZozoFouchtra', 'http://www.codewars.com/users/ZozoFouchtra')
    gen_test_case('colbydauph', 'http://www.codewars.com/users/colbydauph')
