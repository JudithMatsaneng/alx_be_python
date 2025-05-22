hours = 2  # Number of hours to convert

seconds = hours * 3600

hour_str = "hour" if abs(hours) == 1 else "hours"
print(f"{hours} {hour_str} is {seconds} seconds.")
# 2 hours is 7200 seconds.
