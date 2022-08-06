import pandas as pd
import numpy as np
import logging
from typing import Literal


def calc_CDRISC(row: pd.Series, items_num: Literal[10]) -> pd.Series:
    try:
        assert items_num == 10
        if items_num == 10:
            score = calc_CDRISC_10(row)
    except Exception as e:
        logging.error(e, exc_info=True)
        score = np.nan
    finally:
        return pd.Series(score, index=["CDRISC_SCORE"])



def calc_CDRISC_10(row: pd.Series) -> int:
    score = max(10, min(40, row.sum()))
