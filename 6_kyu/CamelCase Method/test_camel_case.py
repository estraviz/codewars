from camel_case import camel_case


def test_camel_case():
    assert camel_case("test case") == "TestCase"
    assert camel_case("camel case method") == "CamelCaseMethod"
    assert camel_case("say hello ") == "SayHello"
    assert camel_case(" camel case word") == "CamelCaseWord"
    assert camel_case("") == ""
