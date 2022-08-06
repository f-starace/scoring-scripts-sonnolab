import pandas as pd
from scipy import stats
from typing import Optional
from .types import InferentialTest



def calc_wilcoxon_ranksum(
    qualitative_param: pd.Series, quantitative_param: pd.Series, alpha: float = 0.05
) -> Optional[InferentialTest]:
    """Calculates Wilcoxon Rank-sum for two independent samples (Non Parametric)

    Args:
        qualitative_param (pd.Series): A column containing categorical data
        quantitative_param (pd.Series): A column containing numerical data
        alpha (float, optional): Defaults to 0.05.

    Returns:
        dict: statistic, pvalue, dof, meaningful | None
    """
    qualitative_values = qualitative_param.unique()
    if len(qualitative_values) != 2:
        return None

    x = quantitative_param[qualitative_param == qualitative_values[0]]
    y = quantitative_param[qualitative_param == qualitative_values[1]]

    statistic, pvalue = stats.ranksums(x, y)
    meaningful = False if pvalue > alpha else True
    return InferentialTest(
        name="wilcoxon ranksum",
        statistic=statistic,
        pvalue=pvalue,
        meaningful=meaningful,
        parametric=False,
    )
