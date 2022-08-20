from typing import Optional
import pandas as pd
from scipy import stats
from .types import InferentialTest

def calc_fisher_exact(
    qualitative_param1: pd.Series,
    qualitative_param2: pd.Series,
    alpha: float = 0.05,
    alternative: str = "two-sided",
) -> Optional[dict]:
    """Apply FisherExact for 2x2 Contingency table (Parametric test)

    Args:
        qualitative_param1 (pd.Series): A column containing categorical data
        qualitative_param2 (pd.Series):  A column containing categorical data
        alpha (float, optional): Defaults to 0.05.
        alternative (str, optional): Defaults to "two-sided".

    Returns:
        dict: odds_ratio, pvalue, meaningful | None
    """
    if qualitative_param1.nunique() != 2 or qualitative_param1.nunique() != 2:
        return None
    contingency_table = pd.crosstab(qualitative_param1, qualitative_param2)

    odds_ratio, pvalue = stats.fisher_exact(contingency_table, alternative=alternative)
    meaningful = False if pvalue > alpha else True
    return InferentialTest(
        name="fisher-exact",
        statistic=odds_ratio,
        pvalue=pvalue,
        meaningful=meaningful,
        parametric=True,
    )
