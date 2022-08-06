import pandas as pd
from typing import Optional
from scipy import stats
from .types import InferentialTest



def calc_ttest(
    qualitative_param: pd.Series, quantitative_param: pd.Series, alpha: float = 0.05
) -> Optional[dict]:
    """Calculates T-test for two independent samples of scores (Parametric)

    Args:
        qualitative_param (pd.Series): A column containing categorical data
        quantitative_param (pd.Series): A column containing numerical data
        alpha (float, optional): Defaults to 0.05.

    Returns:
        dict: statistic, pvalue, dof, meaningful
    """
    qualitative_values = qualitative_param.unique()
    if len(qualitative_values) != 2:
        return None

    x = quantitative_param[qualitative_param == qualitative_values[0]]
    y = quantitative_param[qualitative_param == qualitative_values[1]]

    statistic, pvalue = stats.ttest_ind(x, y)
    meaningful = False if pvalue > alpha else True

    return InferentialTest(
        name="t-test",
        statistic=statistic,
        pvalue=pvalue,
        meaningful=meaningful,
        parametric=True,
    )
