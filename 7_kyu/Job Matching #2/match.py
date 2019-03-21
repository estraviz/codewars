"""Job Matching #2
"""


def match(job, candidates):
    matched_candidates = []
    for candidate in candidates:
        if matching_by_equity(job['equity_max'], candidate['desires_equity']) \
           and matching_by_location(job['locations'],
                                    [candidate['current_location']] +
                                    candidate['desired_locations']):
            matched_candidates.append(candidate)
    return matched_candidates


def matching_by_equity(equity_max, desires_equity):
    return not desires_equity or equity_max


def matching_by_location(locations, current_or_desired_locations):
    for location in locations:
        if location in current_or_desired_locations:
            match = True
            break
    else:
        match = False
    return match
