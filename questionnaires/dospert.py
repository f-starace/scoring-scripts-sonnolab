import pandas as pd
import numpy as np


def calc_DOSPERT_F(row: pd.Series) -> pd.Series:
    """Calculate the DOSPERT Financial domain

    Args:
        row (pd.Series): a row of the dataframe

    Returns:
        pd.Series: dospert_f results
    """
    results_index = ["DOSPERT_F_Q1", "DOSPERT_F_Q2", "DOSPERT_F_Q3"]
    try:
        q1 = sum(
            [
                row.DOSPERT_F_01,
                row.DOSPERT_F_04,
                row.DOSPERT_F_07,
                row.DOSPERT_F_10,
                row.DOSPERT_F_13,
                row.DOSPERT_F_16,
                row.DOSPERT_F_19,
                row.DOSPERT_F_22,
            ]
        )
        q2 = sum(
            [
                row.DOSPERT_F_02,
                row.DOSPERT_F_05,
                row.DOSPERT_F_08,
                row.DOSPERT_F_11,
                row.DOSPERT_F_14,
                row.DOSPERT_F_17,
                row.DOSPERT_F_20,
                row.DOSPERT_F_23,
            ]
        )
        q3 = sum(
            [
                row.DOSPERT_F_03,
                row.DOSPERT_F_06,
                row.DOSPERT_F_09,
                row.DOSPERT_F_12,
                row.DOSPERT_F_15,
                row.DOSPERT_F_18,
                row.DOSPERT_F_21,
                row.DOSPERT_F_24,
            ]
        )
        results = [q1, q2, q3]
    except:
        results = [np.nan, np.nan, np.nan]

    return pd.Series(results, index=results_index)




# TODO: implement other domanis
def calc_DOSPERT(row: pd.Series) -> pd.Series:
    pass