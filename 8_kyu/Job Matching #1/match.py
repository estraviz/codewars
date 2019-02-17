"""Job Matching #1
"""


def match(candidate, job):
    return candidate_has_min_salary(candidate) and \
           job_has_max_salary(job) and \
           is_valid_salary(candidate, job)


def candidate_has_min_salary(candidate):
    return 'min_salary' in candidate.keys()


def job_has_max_salary(job):
    return 'max_salary' in job.keys()


def is_valid_salary(candidate, job):
    return candidate['min_salary']*(1 - 0.10) <= job['max_salary']
