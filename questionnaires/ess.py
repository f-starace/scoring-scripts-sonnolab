import pandas as pd
import numpy as np
import logging




def calc_ESS(row: pd.Series) -> pd.Series:
    try:
        total = row.sum()

        if total < 7:
            cat = "normal"
        elif total < 9:
            cat = "medium sleepiness"
        else:
            cat = "abnormal sleepiness"
        return pd.Series([total, cat], index=["ESS_TOTAL", "ESS_CAT"])

    except Exception as e:
        logging.error(e, exc_info=True)
        return pd.Series([np.nan, np.nan], index=["ESS_TOTAL", "ESS_CAT"])
