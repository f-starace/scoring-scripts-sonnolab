import pandas as pd
import numpy as np
import logging




def calc_ESS(row: pd.Series) -> pd.Series:
    """Calculates ESS total and category"""
    results_index = ["ESS_total", "ESS_category"]
    try:
        total = row.sum()

        if total < 7:
            cat = "normal"
        elif total < 9:
            cat = "medium sleepiness"
        else:
            cat = "abnormal sleepiness"
        results = [total, cat]
        
    except Exception as e:
        logging.error(e, exc_info=True)
        results = [np.nan, np.nan]

    finally:
        return pd.Series(results, index=results_index)

