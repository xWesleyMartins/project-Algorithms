def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    counter = 0

    for start, end in permanence_period:
        if not (isinstance(start, int) and isinstance(end, int)):
            return None

        if start <= target_time <= end:
            counter += 1

    return counter
