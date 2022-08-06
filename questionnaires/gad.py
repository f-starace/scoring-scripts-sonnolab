import pandas as pd
import numpy as np
import logging



def calc_GAD7(row: pd.Series) -> pd.Series:
    try:
        total = row.sum()
        if total < 5:
            cat = "minimal anxiety"
        elif total < 10:
            cat = "mild anxiety"
        elif total < 15:
            cat = "moderate anxiety"
        else:
            cat = "severe anxiety"
        return pd.Series([total, cat], index=["GAD7_TOTAL", "GAD7_CAT"])

    except Exception as e:
        logging.error(e, exc_info=True)
        return pd.Series([np.nan, np.nan], index=["GAD7_TOTAL", "GAD7_CAT"])
