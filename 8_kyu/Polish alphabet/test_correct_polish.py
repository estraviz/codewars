from correct_polish import correct_polish_letters


def test_correct_polish():
    assert correct_polish_letters("Jędrzej Błądziński") == "Jedrzej Bladzinski"
    assert correct_polish_letters("Lech Wałęsa") == "Lech Walesa"

    input_ = "Maria Skłodowska-Curie"
    output = "Maria Sklodowska-Curie"
    assert correct_polish_letters(input_) == output

    assert correct_polish_letters("Władysław Reymont") == "Wladyslaw Reymont"
    assert correct_polish_letters("Mikołaj Kopernik") == "Mikolaj Kopernik"
    assert correct_polish_letters("Józef Piłsudski") == "Jozef Pilsudski"
    assert correct_polish_letters("Czesław Miłosz") == "Czeslaw Milosz"

    input_ = "Agnieszka Radwańska"
    output = "Agnieszka Radwanska"
    assert correct_polish_letters(input_) == output

    assert correct_polish_letters("Wojciech Szczęsny") == "Wojciech Szczesny"
    assert correct_polish_letters("Zażółć gęślą jaźń") == "Zazolc gesla jazn"

    input_ = "Wół go pyta: 'Panie chrząszczu,Po co pan tak brzęczy w gąszczu?'"
    output = "Wol go pyta: 'Panie chrzaszczu,Po co pan tak brzeczy w gaszczu?'"
    assert correct_polish_letters(input_) == output
