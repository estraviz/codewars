# Monotone travel
import pandas as pd


def is_monotone(heights):
    return pd.Series(heights, dtype='float64').is_monotonic
