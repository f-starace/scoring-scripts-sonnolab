import pandas as pd
from datetime import datetime
from .utils.handle_time import calc_age
import numpy as np



# TODO: test if this works

def calc_Profiling(row: pd.Series) -> pd.Series:

    [age, sex, weight, height, bmi] = np.empty(5)

    sex = row.get("sex")
    weight = row.get("weight")
    height = row.get("heigth")
    birth_date = row.get("birth_date")
    submission_date = row.get("submitted_at")


    if weight and height:
        bmi = round(weight / (height) ** 2, 2)

    if birth_date and submission_date:    
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        submission_date = datetime.combine(
            datetime.strptime(submission_date[:10], "%Y-%m-%d").date(),
            datetime.min.time(),
        )
        age = calc_age(birth_date, submission_date)

    return pd.Series(
        [age, sex, weight, height, bmi], index=["AGE", "SEX", "WEIGHT", "HEIGHT", "BMI"]
    )
