# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.

def time_in_milliseconds(h, m, s):
    total_milliseconds = (h * 60 * 60 + m * 60 + s) * 1000
    return total_milliseconds

