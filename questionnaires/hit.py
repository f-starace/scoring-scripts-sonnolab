import pandas as pd
import numpy as np
import logging


HIT_DTC = {"Mai": 6, "Raramente": 8, "Qualche volta": 10, "Molto spesso": 11, "Sempre": 13}


# TODO: prepare for multiple item types

def calc_HIT6(row: pd.Series) -> pd.Series:
    """Returns HIT6 total"""

    try:
        row = row.apply(lambda item: HIT_DTC[item])
    except KeyError as e:
        logging.error(e, exc_info=True)
        row = row.apply(lambda item: np.nan)
    finally:
        score = row.sum()
        return pd.Series([score], index=["HIT6_TOTAL"])
