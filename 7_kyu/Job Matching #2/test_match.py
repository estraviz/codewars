from match import match


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


def test_match():
    assert len(match(job1, candidates)) == 0
    assert len(match(job2, candidates)) == 2
