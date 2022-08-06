
import logging
import pandas as pd
import numpy as np
from datetime import time, timedelta
from .utils.handle_time import time_difference,  parse_time, parse_timedelta, add_time_duration


def calc_MCTQ(row: pd.Series) -> pd.Series:
    try:
        bed_time_work: time = parse_time(row.MCTQ_04)
        ready_to_sleep_work: time = parse_time(row.MCTQ_05)
        sleep_lat_work: timedelta = parse_timedelta(row.MCTQ_06)
        sleep_end_work: time = parse_time(row.MCTQ_07)
        sleep_inertia_work: timedelta = parse_timedelta(row.MCTQ_08)
        use_alarm_work: bool = row.MCTQ_09
        wake_before_alarm_work: bool = row.MCTQ_10
        light_exp_work: timedelta = parse_timedelta(row.MCTQ_11)

        bed_time_free: time = parse_time(row.MCTQ_12)
        ready_to_sleep_free: time = parse_time(row.MCTQ_13)
        sleep_lat_free: timedelta = parse_timedelta(row.MCTQ_14)
        sleep_end_free: time = parse_time(row.MCTQ_15)
        sleep_inertia_free: timedelta = parse_timedelta(row.MCTQ_16)
        use_alarm_free: bool = row.MCTQ_17
        light_exp_free: timedelta = parse_timedelta(row.MCTQ_20)

        work_days: int = row.MCTQ_03
        free_days = 7 - work_days

        # ?computed values

        sleep_onset_work = add_time_duration(ready_to_sleep_work, sleep_lat_work)
        sleep_onset_free = add_time_duration(ready_to_sleep_free, sleep_lat_free)

        time_off_bed_work = add_time_duration(sleep_end_work, sleep_inertia_work)
        time_off_bed_free = add_time_duration(sleep_end_free, sleep_inertia_free)

        sleep_dur_work = time_difference(sleep_end_work, sleep_onset_work)
        sleep_dur_free = time_difference(sleep_end_free, sleep_onset_free)

        time_in_bed_work = time_difference(sleep_end_work, bed_time_work)
        time_in_bed_free = time_difference(sleep_end_free, bed_time_free)

        # mid-sleep
        ms_work = add_time_duration(sleep_onset_work, sleep_dur_work / 2)
        ms_free = add_time_duration(sleep_onset_free, sleep_dur_free / 2)

        # ? combined work and free days variables
        sleep_dur_avg = (sleep_dur_work * work_days + sleep_dur_free * free_days) / 7

        if use_alarm_free == False and sleep_dur_free <= sleep_dur_work:
            chronotype = ms_free
        elif use_alarm_free == False and sleep_dur_free > sleep_dur_work:
            chronotype: time = ms_free - (sleep_dur_free - sleep_dur_avg) / 2
        else:
            chronotype = False
        if sleep_dur_avg > sleep_dur_work:
            weekly_sleep_loss = (sleep_dur_avg - sleep_dur_work) * work_days
        else:
            weekly_sleep_loss = (sleep_dur_avg - sleep_dur_free) * free_days

        rel_social_jetlag = time_difference(ms_free, ms_work)
        abs_social_jetlag = abs(rel_social_jetlag)
        light_exp_avg = (light_exp_work * work_days + light_exp_free * free_days) / 7
        results = [
                bed_time_work,
                bed_time_free,
                ready_to_sleep_work,
                ready_to_sleep_free,
                sleep_lat_work,
                sleep_lat_free,
                sleep_end_work,
                sleep_end_free,
                sleep_inertia_work,
                sleep_inertia_free,
                use_alarm_work,
                use_alarm_free,
                wake_before_alarm_work,
                light_exp_work,
                light_exp_free,
                light_exp_avg,
                work_days,
                free_days,
                sleep_onset_work,
                sleep_onset_free,
                time_off_bed_work,
                time_off_bed_free,
                sleep_dur_work,
                sleep_dur_free,
                sleep_dur_avg,
                time_in_bed_work,
                time_in_bed_free,
                ms_work,
                ms_free,
                chronotype,
                weekly_sleep_loss,
                rel_social_jetlag,
                abs_social_jetlag,
            ]
    
    except Exception as e:
        logging.error(e, exc_info=True)
        results = np.empty(shape=33)

    finally:
        return pd.Series(
            results,
            index=[
                "MCTQ bed_time_work",
                "MCTQ bed_time_free",
                "MCTQ ready_to_sleep_work",
                "MCTQ ready_to_sleep_free",
                "MCTQ sleep_latency_work",
                "MCTQ sleep_latency_free",
                "MCTQ sleep_end_work",
                "MCTQ sleep_end_free",
                "MCTQ sleep_inertia_work",
                "MCTQ sleep_inertia_free",
                "MCTQ use_alarm_work",
                "MCTQ use_alarm_free",
                "MCTQ wake_before_alarm_work",
                "MCTQ light_exp_work",
                "MCTQ light_exp_free",
                "MCTQ light_exp_avg",
                "MCTQ work_days",
                "MCTQ free_days",
                "MCTQ sleep_onset_work",
                "MCTQ sleep_onset_free",
                "MCTQ time_off_bed_work",
                "MCTQ time_off_bed_free",
                "MCTQ sleep_duration_work",
                "MCTQ sleep_duration_free",
                "MCTQ sleep_duration_avg",
                "MCTQ time_in_bed_work",
                "MCTQ time_in_bed_free",
                "MCTQ mid_sleep_work",
                "MCTQ mid_sleep_free",
                "MCTQ chronotype",
                "MCTQ weekly_sleep_loss",
                "MCTQ rel_social_jetlag",
                "MCTQ abs_social_jetlag",
            ],
        )

