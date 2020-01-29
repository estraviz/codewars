"""
N seconds ago
"""

from datetime import datetime, timedelta


def seconds_ago(s, n):
    return str(
        datetime.strptime(s, '%Y-%m-%d %H:%M:%S') - timedelta(seconds=n))
