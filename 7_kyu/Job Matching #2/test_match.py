from match import match


def test_basic_tests():
    candidates = [{
        'desires_equity': True,
        'current_location': 'New York',
        'desired_locations': ['San Francisco', 'Los Angeles']
    }, {
        'desires_equity': False,
        'current_location': 'San Francisco',
        'desired_locations': ['Kentucky', 'New Mexico']
    }]
    job1 = {'equity_max': 0, 'locations': ['Los Angeles', 'New York']}
    job2 = {'equity_max': 1.2, 'locations': ['New York', 'Kentucky']}

    assert len(match(job1, candidates)) == 0
    assert len(match(job2, candidates)) == 2


def test_should_match_candidates_currently_in_a_job_location():
    candidates = map(lambda a: {'desires_equity': False, 'current_location': a,
                                'desired_locations': []},
                     ['NY', 'SF', 'LA', 'CO'])
    job = {'equity_max': 0, 'locations': ['NY', 'SF', 'LA']}

    assert len(match(job, candidates)) == 3


def test_should_match_candidates_desire_to_move_to_a_job_location():
    candidates = map(lambda a: {'desires_equity': True,
                                'current_location': 'WY',
                                'desired_locations': a},
                     [['NY', 'SF'], ['LA'], ['CO'], ['ME'], ['LA', 'WA']])
    job = {'equity_max': 1.2, 'locations': ['NY', 'SF', 'CO', 'WA']}

    assert len(match(job, candidates)) == 3


def test_should_not_match_candidates_when_equity_is_desired_but_not_offered():
    candidates = map(lambda a: {'desires_equity': True, 'current_location': a,
                                'desired_locations': []},
                     ['NY', 'SF', 'LA', 'CO'])
    job = {'equity_max': 0, 'locations': ['NY', 'SF', 'LA']}

    assert len(match(job, candidates)) == 0
