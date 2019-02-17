from match import match


candidate1 = {'min_salary': 120000}
candidate2 = {'min_salary': 190000}

job1 = {'max_salary': 130000}
job2 = {'max_salary': 80000}
job3 = {'max_salary': 171000}


def test_valid_matches():
    assert match(candidate1, job1) is True
    assert match(candidate1, job3) is True
    assert match(candidate2, job3) is True


def test_invalid_matches():
    assert match(candidate1, job2) is False
    assert match(candidate2, job1) is False
    assert match(candidate2, job2) is False
