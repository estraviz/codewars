from solution import remove_parentheses
import pytest


@pytest.mark.parametrize(
    "string, output",
    [("example(unwanted thing)example", "exampleexample"),
     ("example (unwanted thing) example", "example  example"),
     ("a (bc d)e", "a e"),
     ("a(b(c))", "a"),
     ("hello example (words(more words) here) something",
      "hello example  something"),
     ("(first group) (second group) (third group)", "  ")
    ]
)
def test_remove_parentheses(string, output):
    assert remove_parentheses(string) == output
