import pandas as pd
from scipy import stats
from .types import InferentialTest



def calc_chisquare(
    qualitative_param1: pd.Series, qualitative_param2: pd.Series, alpha: float = 0.05
) -> InferentialTest:
    """Calculate a one-way chi-square test (Non Parametric)

    Args:
        qualitative_param1 (pd.Series): A column containing categorical data
        qualitative_param2 (pd.Series): A column containing categorical data
        alpha (float, optional): Defaults to 0.05.

    Returns:
        dict: statistic, pvalue, dof, meaningful
    """
    contingency_table = pd.crosstab(qualitative_param1, qualitative_param2)
    statistic, pvalue, dof, _ = stats.chi2_contingency(
        contingency_table
    )  # excluded expected frequencies from result
    meaningful = False if pvalue > alpha else True
    return InferentialTest(
        name="chi-square",
        statistic=statistic,
        pvalue=pvalue,
        meaningful=meaningful,
        parametric=False,
    )
