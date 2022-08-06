import pandas as pd
from scipy import stats
from .types import InferentialTest



def calc_spearman(
    quantitative_param1: pd.Series, quantitative_param2: pd.Series, alpha: float = 0.05
) -> InferentialTest:
    """Applies Spearson Test for two quantitative params (Non Parametric Test)

    Args:
        quantitative_param1 (pd.Series): A column containing numbers
        quantitative_param2 (pd.Series): A column containing numbers
        alpha (float, optional) Defaults to 0.05.

    Returns:
        dict: statistic, pvalue, meaningful
    """
    statistic, pvalue = stats.spearmanr(quantitative_param1, quantitative_param2)
    meaningful = False if pvalue > alpha else True
    return InferentialTest(
        name="spearman",
        statistic=statistic,
        pvalue=pvalue,
        meaningful=meaningful,
        parametric=False,
    )
