import pandas as pd
import numpy as np
import logging


# TODO: prepare for multiple item types
def calc_GAD7(row: pd.Series) -> pd.Series:
    results_index = ["GAD7_TOT", "GAD7_CAT"]
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

    except Exception as e:
        logging.error(e, exc_info=True)
        total, cat = np.nan, np.nan

    finally:
        results = [total, cat]
        return pd.Series(results, index=results_index)
