
import logging
import pandas as pd
import numpy as np
from .utils.handle_time import h_to_mins



def calc_sleep_efficiency(
    hours_slept: int, sleep_onset: str, sleep_offset: str
) -> float:
    """Calculates the sleep efficiency
    Args:
        hours_slept (int)
        sleep_onset (str)
        sleep_offset (str)
    """
    sleep_onset = h_to_mins(sleep_onset)
    sleep_offset = h_to_mins(sleep_offset)

    if sleep_onset < h_to_mins("05:00"):
        sleep_dur_m = sleep_offset - sleep_onset
    else:
        sleep_dur_m = sleep_offset - sleep_onset + h_to_mins("24:00")
    sleep_dur_h = sleep_dur_m / 60
    sleep_eff = hours_slept / sleep_dur_h
    return sleep_eff


def generic_PSQI(option: str) -> int:
    if option == "Mai durante il mese passato":
        option = 0
    elif option == "Meno di una volta a settimana":
        option = 1
    elif option == "Una o due volte a settimana":
        option = 2
    elif option == "Tre o più volte a settimana":
        option = 3
    else:
        raise ValueError(
            f"During elaboration of PSQI, an unexpected option has come across {option}"
        )
    return option


def calc_PSQI(row: pd.Series) -> pd.Series:
    """Calculates the PSQI score
    Args:
        row (pd.Series): the row to analyze
    """    
    results_index = ["PSQI_COMP_1","PSQI_COMP_2","PSQI_COMP_3","PSQI_COMP_4","PSQI_COMP_5","PSQI_COMP_6","PSQI_COMP_7","PSQI_TOT","PSQI_CAT"]

    try:
        print(row.values.tolist())
        generic_cols = [
            col
            for col in row.index
            if col in [
                "PSQI_06","PSQI_07", "PSQI_08", "PSQI_09", "PSQI_10", "PSQI_11", "PSQI_12", "PSQI_13", "PSQI_16", 
            ]
            not in [
                "PSQI_01",
                "PSQI_02",
                "PSQI_03",
                "PSQI_04",
                "PSQI_05",
                "PSQI_14",
                "PSQI_15",
                "PSQI_17",
                "PSQI_20",
            ]
        ]

        row[generic_cols] = row[generic_cols].apply(lambda col: generic_PSQI(col))

        if row.PSQI_02 == "Meno di 15 minuti":
            row.PSQI_02 = 0
        elif row.PSQI_02 == "Tra 16 e 30 minuti":
            row.PSQI_02 = 1
        elif row.PSQI_02 == "Tra 31 e 60 minuti":
            row.PSQI_02 = 2
        elif row.PSQI_02 == "Più di 60 minuti":
            row.PSQI_02 = 3
        else:
            raise ValueError(f"Unexpected value at PSQI_02, got {row.PSQI_02}")

        if row.PSQI_05 == "Mai durante il mese passato":
            row.PSQI_05 = 0
        elif row.PSQI_05 == "Meno di una volta a settimana":
            row.PSQI_05 = 1
        elif row.PSQI_05 == "Una o due volte a settimana":
            row.PSQI_05 = 2
        elif row.PSQI_05 == "Tre o più volte a settimana":
            row.PSQI_05 = 3
        else:
            raise ValueError(f"Unexpected value at PSQI_05, got {row.PSQI_05}")

        if row.PSQI_17 == "Molto buona":
            row.PSQI_17 = 0
        elif row.PSQI_17 == "Abbastanza buona":
            row.PSQI_17 = 1
        elif row.PSQI_17 == "Abbastanza cattiva":
            row.PSQI_17 = 2
        elif row.PSQI_17 == "Molto cattiva":
            row.PSQI_17 = 3
        else:
            raise ValueError(f"Unexpected value at PSQI_17, got {row.PSQI_17}")

        if row.PSQI_20 == "Per niente":
            row.PSQI_20 = 0
        elif row.PSQI_20 == "Poco":
            row.PSQI_20 = 1
        elif row.PSQI_20 == "Abbastanza":
            row.PSQI_20 = 2
        elif row.PSQI_20 == "Molto":
            row.PSQI_20 = 3
        else:
            raise ValueError(f"Unexpected value at PSQI_20, got {row.PSQI_20}")

        # comp1 subjective sleep quality
        comp1 = row.PSQI_17

        # comp2 sleep latency
        sleep_lat = row.PSQI_02 + row.PSQI_05

        if sleep_lat == 0 :
            comp2 = 0
        elif sleep_lat == 1 or sleep_lat == 2:
            comp2 = 1
        elif sleep_lat == 3 or sleep_lat == 4:
            comp2 = 2
        else:
            comp2 = 3


        # comp3 sleep duration

        row.PSQI_04 = float(row.PSQI_04)

        if row.PSQI_04 < 5:
            comp3 = 3
        elif row.PSQI_04 >= 5 and row.PSQI_04 < 6:
            comp3 = 2
        elif row.PSQI_04 >= 6 and row.PSQI_04 < 7:
            comp3 = 1
        elif row.PSQI_04 >= 7:
            comp3 = 0

        # comp4 habitual sleep efficiency
        sleep_eff = calc_sleep_efficiency(row.PSQI_04, row.PSQI_01, row.PSQI_03)
        if sleep_eff < 0.65:
            comp4 = 3
        elif sleep_eff < 0.75:
            comp4 = 2
        elif sleep_eff < 0.85:
            comp4 = 1
        else:
            comp4 = 0

        # comp5 sleep disturbances
        comp5_sum = np.sum(
            [
                row.PSQI_05,
                row.PSQI_06,
                row.PSQI_07,
                row.PSQI_08,
                row.PSQI_09,
                row.PSQI_10,
                row.PSQI_11,
                row.PSQI_12,
                row.PSQI_16,
            ]
        )
        if comp5_sum == 0:
            comp5 = 0
        elif comp5_sum < 10:
            comp5 = 1
        elif comp5_sum < 19:
            comp5 = 2
        else:
            comp5 = 3

        # comp6 use of sleeping medication
        comp6 = int(row.PSQI_18)

        # comp7
        comp7_sum = row.PSQI_19 + row.PSQI_20
        if comp7_sum == 0:
            comp7 = 0
        elif comp7_sum < 3:
            comp7 = 1
        elif comp7_sum < 5:
            comp7 = 2
        else:
            comp7 = 3

        total = comp1 + comp2 + comp3 + comp4 + comp5 + comp6 + comp7
        cat = "good sleeper" if total <= 5 else "poor sleeper"

        # wrapping up the results together
        results = [comp1, comp2, comp3, comp4, comp5, comp6, comp7, total, cat]

    except ValueError as e:
        # handle value errors
        logging.error(e, exc_info=True)
        results = np.empty(9)

    except TypeError as e:
        # handle type errors
        logging.error(e, exc_info=True)
        results = np.empty(9)


    finally:         
        return pd.Series( results, index=results_index)



if __name__ == '__main__':
    pass