import datetime
def shift_time(days: int, seconds: int):
    initial_time = datetime.datetime(2023, 1, 1, 12, 30, 0)
    shifted_time = initial_time + datetime.timedelta(days=days, seconds=seconds)
    return (shifted_time.day, shifted_time.second)
days, seconds = 1, 0
print(shift_time(days, seconds))