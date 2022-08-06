import pandas as pd
import numpy as np
import logging

# TODO: prepare for multiple item number

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

    except Exception as e:
        logging.error(e, exc_info=True)
        total, cat = np.nan, np.nan

    finally:
        return pd.Series([total, cat], index=["PHQ9_TOT", "PHQ9_CAT"])
