def parse_latitude(latitude_str):
    # latitude_str is in decimal format
    if len(latitude_str.split(".")) == 2:
        return float(latitude_str)

    direction = latitude_str[0]

    degrees_str, minutes_str, seconds_str, dec_seconds_str = latitude_str[1:].split(".")

    degrees = float(degrees_str)
    minutes = float(minutes_str)
    seconds = float(seconds_str) + float(dec_seconds_str) / 1000

    decimal_degrees = degrees + minutes / 60.0 + seconds / 3600.0

    if direction == "S":
        decimal_degrees *= -1

    return decimal_degrees


def parse_longitude(longitude_str):
    # longitude_str is in decimal format
    if len(longitude_str.split(".")) == 2:
        return float(longitude_str)

    direction = longitude_str[0]

    degrees_str, minutes_str, seconds_str, dec_seconds_str = longitude_str[1:].split(".")

    degrees = float(degrees_str)
    minutes = float(minutes_str)
    seconds = float(seconds_str) + float(dec_seconds_str) / 1000

    decimal_degrees = degrees + minutes / 60.0 + seconds / 3600.0

    if direction == "W":
        decimal_degrees *= -1

    return decimal_degrees
