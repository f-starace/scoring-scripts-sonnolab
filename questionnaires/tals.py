import logging
import pandas as pd
import numpy as np

def calc_TALS(row: pd.Series) -> pd.Series:
    """Return TALS score

    Args:
        row (pd.Series)

    Returns:
        int: TALS_score
    """
    try:
        total = row.sum()
    except Exception as e:
        logging.error(e, exc_info=True)
        total = np.nan
    finally:
        return pd.Series(total, index=["TALS_TOTAL"])

