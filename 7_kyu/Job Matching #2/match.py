"""Job Matching #2
"""


def match(job, candidates):
    filtered_candidates = []
    for candidate in candidates:
        if not candidate['desires_equity'] or \
               candidate['desires_equity'] and job['equity_max'] > 0:
            for job_location in job['locations']:
                if job_location in candidate['current_location'] or \
                   job_location in candidate['desired_locations']:
                    filtered_candidates.append(candidate)
                    break
    return filtered_candidates
