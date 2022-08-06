import pandas as pd
import numpy as np
import logging

def calc_BAI(row: pd.Series) -> pd.Series:
    try:
        total = row.sum()
        if total < 8:
            cat = "minimal anxiety"
        elif total < 16:
            cat = "mild anxiety"
        elif total < 26:
            cat = "moderate anxiety"
        else:
            cat = "severe anxiety"
        return pd.Series([total, cat], index=["BAI_TOTAL", "BAI_CAT"])

    except Exception as e:
        logging.error(e, exc_info=True)
        return pd.Series([np.nan, np.nan], index=["BAI_TOTAL", "BAI_CAT"])
