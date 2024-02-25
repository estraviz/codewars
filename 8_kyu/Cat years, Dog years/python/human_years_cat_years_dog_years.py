'''Cat years, Dog years
'''


CAT = 'cat'
DOG = 'dog'


def human_years_cat_years_dog_years(human_years):
    return [human_years, animal_years(human_years, CAT),
            animal_years(human_years, DOG)]


def animal_multiplier(animal):
    if animal == CAT:
        return 4
    elif animal == DOG:
        return 5
    raise ValueError('Animal in consideration was not of the kind CAT or DOG')


def animal_years(human_years, animal):
    mult = animal_multiplier(animal)
    return 15 if human_years == 1 \
        else 24 if human_years == 2 \
        else 24 + (human_years - 2) * mult
