def is_leap_year(year: int) -> bool:
    """Verifies if a year passed by parameter to the function is a leap year.

    Args:
        year (int): the year to verify.

    Returns:
        bool: whether it is a leap year or not.
    """
    is_leap = False

    if year % 4 == 0:
        is_leap = True

        if year % 100 == 0:
            is_leap = False

            if year % 400 == 0:
                is_leap = True

    return is_leap
