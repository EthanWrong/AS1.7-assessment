"""Code to simplify starting/stopping a timer into a function. Although
this function is so simple it doesn't need to be a function, it is easier to
tell what is going on with the name 'start_timer' than 'time.time'
"""
import time


def start_timer():
    start = time.time()
    return start


def stop_timer():
    stop = time.time()
    return stop


def calc_time(start, stop):
    result = int(stop - start)
    return result


# function that returns a formatted string with the minutes and seconds
def write_min_and_sec(seconds):
    minutes = int(seconds // 60)
    and_seconds = int(seconds % 60)

    if str(minutes)[-1] != "1":
        min_s = "s"
    else:
        min_s = ""

    if str(and_seconds)[-1] != "1":
        sec_s = "s"
    else:
        sec_s = ""

    return f"{minutes} minute{min_s} and {and_seconds} second{sec_s}"


# main routine


user_start = start_timer()
input("Type the letter 'x' >>> ")
input("Type the letter 'y' >>> ")
user_stop = stop_timer()

time = calc_time(user_start, user_stop)
print(f"It took you {write_min_and_sec(time)} to type the letter 'x' and 'y'")
