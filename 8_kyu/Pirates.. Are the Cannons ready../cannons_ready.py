"""
Pirates!! Are the Cannons ready!??
"""


def cannons_ready(gunners):
    return 'Fire!' if len(gunners) == sum(
        1 for readiness in gunners.values()
        if readiness == 'aye') else 'Shiver me timbers!'
