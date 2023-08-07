import logging as log
from datetime import date
from ParentalControl.Auth import write_use_time, read_use_time


def read_elapsed_time_data():
    current_date = str(date.today())
    elapsed_time = 0
    try:
        rows = read_use_time()
        rows.reverse()
        if len(rows) >= 1 and rows[0][0] == current_date:
            elapsed_time = int(rows[0][1])
    except FileNotFoundError:
        log.warning("Usage time record not found.")
    except Exception as e:
        print(e)
        pass
    return elapsed_time


def save_elapsed_time_data(elapsed_time):
    log.info(f"Time: {elapsed_time}")
    current_date = str(date.today())
    elapsed_time = str(elapsed_time)
    try:
        rows = read_use_time()
        rows.reverse()
        if rows:
            newest_date = rows[0][0]
            if newest_date == current_date:
                rows[0][1] = elapsed_time
                rows.reverse()
            else:
                rows.reverse()
                rows.append([current_date, elapsed_time])
        else:
            rows.reverse()
            rows.append([current_date, elapsed_time])
        log.debug(f"Elapsed Time: {current_date},{elapsed_time}")
        write_use_time(rows)

    except FileNotFoundError:
        rows = [[current_date, elapsed_time]]
        write_use_time(rows)


def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    temp_time = f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"
    return temp_time
