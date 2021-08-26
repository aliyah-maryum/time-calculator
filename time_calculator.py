def add_time(start_time, duration_time, day=""):

    start_without_AMPM = start_time.split(" ")[0]
    start_hour = int(start_without_AMPM.split(":")[0])
    start_minutes = int(start_without_AMPM.split(":")[1])
    
    duration_hour = int(duration_time.split(":")[0])
    duration_minutes = int(duration_time.split(":")[1])

    total_minutes = start_minutes + duration_minutes

    if total_minutes >= 60:
        start_hour = start_hour + 1
        total_minutes = total_minutes % 60

    total_hour = start_hour + duration_hour

    end_hour = total_hour % 12
    total_minutes = "0" + str(total_minutes) if total_minutes <= 9 else str(total_minutes)

    end_hour = 12 if end_hour == 0 else end_hour

    AMPM = start_time.split(" ")[1]
    AMPM_switch = {"AM" : "PM", "PM" : "AM"}
    AMPM_switch_amt = total_hour // 12 #gives 39

    extra_days = total_hour // 24
    if (AMPM == "PM") and (start_hour + (duration_hour % 12) >= 12):
      extra_days = extra_days + 1

    AMPM = AMPM_switch[AMPM] if (AMPM_switch_amt % 2 == 1) else AMPM

    week_days_dict = {"monday" : 0, "tuesday" : 1, "wednesday" : 2, "thursday" : 3, "friday" : 4, "saturday" : 5, "sunday" : 6}
    week_days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    added_time = str(end_hour) + ":" + str(total_minutes) + " " + AMPM

    if day != "":
        day = day.lower()
        pos = int(week_days_dict[day] + extra_days) % 7
        new_day = week_days_list[pos]
        added_time += ", " + new_day

    if extra_days == 1:
        added_time = added_time + " " + "(next day)"
    elif extra_days > 1:
        added_time = added_time + " (" + str(extra_days) + " days later)"

    return added_time
