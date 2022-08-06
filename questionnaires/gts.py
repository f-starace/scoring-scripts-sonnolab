import pandas as pd
import numpy as np

def calc_GTS(row: pd.Series) -> pd.Series:
    try:
        score = round(
            np.mean(
                [row.GTS_01, row.GTS_02, row.GTS_03, row.GTS_04, row.GTS_05, row.GTS_06]
            ),
            4,
        )
    except:
        score = np.nan
    return pd.Series(score, index=["GTS_SCORE"])
