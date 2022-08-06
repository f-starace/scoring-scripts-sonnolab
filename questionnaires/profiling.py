import pandas as pd
from datetime import datetime
from .utils.handle_time import calc_age



def calc_Anagrafica(row: pd.Series) -> pd.Series:
    birth_date = datetime.strptime(row["birth_date"], "%Y-%m-%d")
    submission_date = datetime.combine(
        datetime.strptime(row["submitted_at"][:10], "%Y-%m-%d").date(),
        datetime.min.time(),
    )
    weight = row["weight"]
    height = row["heigth"]
    sex = row["sex"]

    bmi = round(weight / (height) ** 2, 2)
    age = calc_age(birth_date, submission_date)

    return pd.Series(
        [age, sex, weight, height, bmi], index=["AGE", "SEX", "WEIGHT", "HEIGHT", "BMI"]
    )
