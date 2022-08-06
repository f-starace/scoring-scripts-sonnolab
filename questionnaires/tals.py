import pandas as pd
import numpy as np

def calc_TALS(row: pd.Series) -> pd.Series:
    """Returns TALS score

    Args:
        row (pd.Series)

    Returns:
        int: TALS_score
    """
    try:
        total = row.sum()
        return pd.Series(total, index=["TALS_TOTAL"])
    except Exception as e:
        print(e)
        return pd.Series(np.nan, index=["TALS_TOTAL"])
