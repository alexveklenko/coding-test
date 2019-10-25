def get_temperature_closest_to_zero(temperatures):

    first_min = min(temperatures, key=abs, default=0)

    if abs(first_min) in temperatures:
        return abs(first_min)

    return first_min
