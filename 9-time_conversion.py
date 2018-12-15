time = input().strip()
am_or_pm = (time[8:10] == "PM")

if am_or_pm:
    hours = int(time[0:2])
    if hours != 12:
        hours += 12
    res = format(hours, "02") + time[2:8]
    print(res)

elif time[0:2] == "12":
    print("00" + time[2:8])

else:
    print(time[0:8])
