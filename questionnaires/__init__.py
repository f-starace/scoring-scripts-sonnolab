import pandas as pd
from typing import Callable




# used for barrel export
from .bai import calc_BAI
from .cdrisc import calc_CDRISC
from .dospert import calc_DOSPERT
from .ess import calc_ESS
from .gad import calc_GAD7
from .gts import calc_GTS
from .hit import calc_HIT6
from .mctq import calc_MCTQ
from .midas import calc_MIDAS
from .moods import calc_MOODS
from .phq import calc_PHQ9
from .profiling import calc_Profiling
from .psqi import calc_PSQI
from .rmeq import calc_RMEQ
from .tals import calc_TALS




# TODO: test this function
def mapply(df: pd.DataFrame, func: Callable) -> pd.DataFrame:
    """
    Apply a function to each row of a dataframe.
    """
    cols = [df[c] for c in df.columns]
    return list(map(func, * cols))



def format_string(string: str) -> str:
    """
    Remove punctuation from string, remove accents, strip it and convert to lowercase.
    """
    return string.strip().lower().translate(str.maketrans('', '', string.punctuation))





