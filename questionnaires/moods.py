import logging
import pandas as pd
import numpy as np


def calc_MOODS(row: pd.Series) -> pd.Series:
    """Returns MOODS total

    Args:
        row (pd.Series)

    Returns:
        int: MOODS total
    """
    try:
        total = row.sum()
    except Exception as e:
        logging.error(e, exc_info=True)
        total = np.nan
    finally:
        return pd.Series(total, index=["MOODS_TOT"])
