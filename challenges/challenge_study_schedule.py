def study_schedule(permanence_period, target_time):

    try:
        for start, exit in permanence_period:
            students = 0

            if start <= target_time <= exit:
                students += 1

        return students

    except TypeError:
        return None
