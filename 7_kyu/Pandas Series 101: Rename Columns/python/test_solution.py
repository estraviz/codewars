import pandas as pd
import pytest
from solution import rename_columns


@pytest.mark.parametrize(
    "df_input, names, df_output",
    [
        [
            pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=list("123")),
            ("A", "B", "C"),
            pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=list("ABC")),
        ]
    ],
)
def test_rename_columns(df_input, names, df_output):
    assert rename_columns(df_input, names).equals(df_output)
