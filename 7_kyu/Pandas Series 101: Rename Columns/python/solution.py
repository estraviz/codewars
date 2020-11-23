"""
Pandas Series 101: Rename Columns
"""

import pandas as pd


def rename_columns(df, names):
    new_df = pd.DataFrame.copy(df)
    new_df.columns = names
    return new_df
