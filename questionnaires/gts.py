import logging
import pandas as pd
import numpy as np

def calc_GTS(row: pd.Series) -> pd.Series:
    try:
        score = round(
            np.mean(
                [row.GTS_01, row.GTS_02, row.GTS_03, row.GTS_04, row.GTS_05, row.GTS_06]
            ),
            4,
        )
    except Exception as e:
        logging.error(e, exc_info=True)
        score = np.nan
    finally:
        return pd.Series(score, index=["GTS_SCORE"])
