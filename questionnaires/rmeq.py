import logging
import pandas as pd
import numpy as np


def calc_RMEQ(row: pd.Series) -> pd.Series:
    """Calculates the RMEQ tot and cat from a pd.Series row."

    Args:
        row (pd.Series): the pd.Series of the record

    Returns:
        total, cat
    """
    q1 = {
        "Prima delle 06:30": 5,
        "Tra le 06:30 e le 07:45": 4,
        "Tra le 07:45 e le 09:45": 3,
        "Tra le 09:45 e le 10:45": 2,
        "Dopo le 10:45": 1,
    }
    q2 = {
        "Molto stanco/a": 1,
        "Abbastanza stanco/a": 2,
        "Abbastanza riposato/a": 3,
        "Molto riposato/a": 4,
    }

    q3 = {
        "Prima delle 21": 5,
        "Tra le 21 e le 22:15": 4,
        "Tra le 22:15 e le 00:30": 3,
        "Tra le 00:30 e le 02:15": 2,
        "Dopo le 02:15": 1,
    }
    q4 = {
        "Tra le 04:00 e le 08:00": 5,
        "Tra le 08:00 e le 10:00": 4,
        "Tra le 10:00 e le 16:00": 3,
        "Tra le 16:00 e le 20:00": 2,
        "Dopo le 20:00": 1,
    }

    q5 = {
        "Decisamente più attivo/a al mattino": 6,
        "Un po’ più attivo/a la mattina rispetto alla sera": 4,
        "Un po’ più attivo/a la sera rispetto alla mattina": 2,
        "Decisamente più attivo/a alla sera": 0,
    }

    try:

        points = [
            q1[row.RMEQ_01],
            q2[row.RMEQ_02],
            q3[row.RMEQ_03],
            q4[row.RMEQ_04],
            q5[row.RMEQ_05],
        ]
        # assign tot
        total = sum(points)
        # assign cat
        if total <= 10:
            cat = "ET"
        elif total <= 18:
            cat = "NT"
        elif total >= 19:
            cat = "MT"

    except KeyError as e:
        logging.error(e, exc_info=True)
        total, cat = np.nan, np.nan
    finally:
        return pd.Series([total, cat], index=["RMEQ_TOT", "RMEQ_CAT"])
