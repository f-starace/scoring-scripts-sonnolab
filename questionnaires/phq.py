import pandas as pd
import numpy as np
import logging


def calc_PHQ9(row: pd.Series) -> pd.Series:
    try:
        total = row.sum()

        if total < 5:
            cat = "no symptoms"
        elif total < 10:
            cat = "minimal symptoms"
        elif total < 15:
            cat = "minor depression / dysthymia / mild mayor depression"
        elif total < 20:
            cat = "moderately severe mayor depression"
        else:
            cat = "severe mayor depression"
        return pd.Series([total, cat], index=["PHQ9_TOTAL", "PHQ9_CAT"])

    except Exception as e:
        logging.error(e, exc_info=True)
        return pd.Series([np.nan, np.nan], index=["PHQ9_TOTAL", "PHQ9_CAT"])
