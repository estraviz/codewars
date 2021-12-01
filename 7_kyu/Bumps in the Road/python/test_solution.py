import codewars_test as test
from solution import bumps


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(bumps("n"), "Woohoo!")
        test.assert_equals(bumps("_nnnnnnn_n__n______nn__nn_nnn"), "Car Dead")
        test.assert_equals(bumps("______n___n_"), "Woohoo!")
        test.assert_equals(bumps("nnnnnnnnnnnnnnnnnnnnn"), "Car Dead")
