from solution import count_languages


def test_example_case():
    list1 = [
        {
            'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland',
            'continent': 'Europe', 'age': 19, 'language': 'C'
        },
        {
            'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein',
            'continent': 'Europe', 'age': 52, 'language': 'JavaScript'
        },
        {
            'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay',
            'continent': 'Americas', 'age': 29, 'language': 'Ruby'
        },
        {
            'firstName': 'George', 'lastName': 'B.', 'country': 'England',
            'continent': 'Europe', 'age': 81, 'language': 'C'
        },
    ]
    answer = {'C': 2, 'JavaScript': 1, 'Ruby': 1}
    assert count_languages(list1) == answer
