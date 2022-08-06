from datetime import datetime, time, timedelta, date


def h_to_mins(hour_str: str) -> int:
    h, m = hour_str.split(":")
    minutes = int(h) * 60 + int(m)
    return minutes


def calc_age(prev_date: datetime, nex_date: datetime = datetime.today()) -> int:
    """Compute the difference in years between two datetime objects
    Args:
        prev_date (datetime): the date to analyze
        nex_date (datetime, optional). Defaults to datetime.today().

    Returns:
        int: number of years
    """
    return round((nex_date - prev_date).days / 365)


def add_time_duration(initial_time: time, time_duration: timedelta) -> time:
    """Adds two times objects together

    Args:
        time1 (time): first time
        time2 (time): the dur

    Returns:
        final_time
    """
    initial_dt = datetime.combine(date.today(), initial_time)
    final_time = (initial_dt + time_duration).time()
    return final_time


def time_difference(post_time: time, pre_time: time) -> timedelta:
    """Perform subtraction of time

    Args:
        post_time (time): final_time
        pre_time (time): previous_time

    Returns:
        time_duration (time)
    """
    pre_dt = datetime.combine(date.today(), pre_time)
    post_dt = datetime.combine(date.today(), post_time)
    if pre_dt >= post_dt:
        pre_dt = pre_dt - timedelta(days=1)
    time_duration = post_dt - pre_dt
    return time_duration


def parse_time(time_str: str) -> time:
    if type(time_str) == time:
        return time_str
    return datetime.strptime(time_str, "%H:%M").time()


def parse_timedelta(time_str: str) -> timedelta:
    if type(time_str) == time:
        dt = time_str
    else:
        dt = datetime.strptime(time_str, "%H:%M")
    return timedelta(hours=dt.hour, minutes=dt.minute)
