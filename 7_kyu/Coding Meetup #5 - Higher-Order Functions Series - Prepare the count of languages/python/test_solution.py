from solution import count_languages


def test_example_case_1():
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
    answer1 = {'C': 2, 'JavaScript': 1, 'Ruby': 1}
    assert count_languages(list1) == answer1


def test_example_case_2():
    list2 = [
        {
            'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus',
            'continent': 'Europe', 'age': 29, 'language': 'JavaScript'
        },
        {
            'firstName': 'Amar', 'lastName': 'V.',
            'country': 'Bosnia and Herzegovina', 'continent': 'Europe',
            'age': 32, 'language': 'Ruby'
        },
    ]
    answer2 = {'Ruby': 1, 'JavaScript': 1}
    assert count_languages(list2) == answer2


def test_example_case_3():
    list3 = [
        {
            'firstName': 'Sofia', 'lastName': 'P.', 'country': 'Italy',
            'continent': 'Europe', 'age': 41, 'language': 'Clojure'
        },
        {
            'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica',
            'continent': 'Americas', 'age': 42, 'language': 'JavaScript'
        },
        {
            'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan',
            'continent': 'Asia', 'age': 43, 'language': 'Python'
        },
        {
            'firstName': 'Rimas', 'lastName': 'C.', 'country': 'Jordan',
            'continent': 'Asia', 'age': 44, 'language': 'Java'
        }
    ]
    answer3 = {'Clojure': 1, 'JavaScript': 1, 'Python': 1, 'Java': 1}
    assert count_languages(list3) == answer3


def test_example_case_4():
    list4 = [
        { 'firstName': 'Alexander', 'lastName': 'F.', 'country': 'Russia', 'continent': 'Europe', 'age': 89, 'language': 'Java' },
        { 'firstName': 'Fatima', 'lastName': 'K.', 'country': 'Saudi Arabia', 'continent': 'Asia', 'age': 21, 'language': 'Clojure' },
        { 'firstName': 'Mark', 'lastName': 'G.', 'country': 'Scotland', 'continent': 'Europe', 'age': 22, 'language': 'JavaScript' },
        { 'firstName': 'Nikola', 'lastName': 'H.', 'country': 'Serbia', 'continent': 'Europe', 'age': 29, 'language': 'Python' },
        { 'firstName': 'Jakub', 'lastName': 'I.', 'country': 'Slovakia', 'continent': 'Europe', 'age': 28, 'language': 'Java' },
        { 'firstName': 'Luka', 'lastName': 'J.', 'country': 'Slovenia', 'continent': 'Europe', 'age': 29, 'language': 'Clojure' }
        ]
    answer4 = { 'Clojure': 2, 'JavaScript': 1, 'Python': 1, 'Java': 2 }
    assert count_languages(list4) == answer4


def test_example_case_5():
    list5 = [
        {
            'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan',
            'continent': 'Asia', 'age': 30, 'language': 'Ruby'
        },
        {
            'firstName': 'Mehdi', 'lastName': 'H.', 'country': 'Tunisia',
            'continent': 'Africa', 'age': 42, 'language': 'Python'
        },
        {
            'firstName': 'Yusuf', 'lastName': 'N.', 'country': 'Turkey',
            'continent': 'Europe', 'age': 22, 'language': 'Python'
        },
        {
            'firstName': 'Artem', 'lastName': 'O.', 'country': 'Ukraine',
            'continent': 'Europe', 'age': 29, 'language': 'Java'
        }
    ]
    answer5 = {'Ruby': 1, 'Java': 1, 'Python': 2}
    assert count_languages(list5) == answer5
