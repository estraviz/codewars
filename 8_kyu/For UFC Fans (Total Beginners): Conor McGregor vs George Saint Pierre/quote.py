"""
For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre
"""


def quote(fighter):
    return {
        'george saint pierre':
        "I am not impressed by your performance.",
        'conor mcgregor':
        "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    }.get(' '.join(word.lower() for word in fighter.split()))
