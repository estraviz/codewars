from human_years_cat_years_dog_years import human_years_cat_years_dog_years


def test_human_years_cat_years_dog_years():
    assert human_years_cat_years_dog_years(1) == [1, 15, 15]
    assert human_years_cat_years_dog_years(2) == [2, 24, 24]
    assert human_years_cat_years_dog_years(10) == [10, 56, 64]
    assert human_years_cat_years_dog_years(23) == [23, 108, 129]
    assert human_years_cat_years_dog_years(25) == [25, 116, 139]
