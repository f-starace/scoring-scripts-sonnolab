import pandas as pd
import numpy as np
import logging


def calc_MIDAS(row: pd.Series) -> pd.Series:
    try:
        total = row.sum()
        if total < 6:
            cat = "I"
        elif total < 11:
            cat = "II"
        elif total < 21:
            cat = "III"
        else:
            cat = "IV"
    except Exception as e:
        logging.error(e, exc_info=True)

    finally:
        results = [total, cat]

        return pd.Series([np.nan, np.nan], index=["MIDAS_TOT", "MIDAS_CAT"])
