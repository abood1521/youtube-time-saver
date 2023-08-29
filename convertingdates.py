# youtube api --> year-month-day ---> 2023-04-02
# The time module ---> day/month/year ---> 14/02/2023
import datetime
date_time = datetime.date.today()
print(date_time)
def convert_dates(s: str):
    d, m, y = s.split("/")
    return "-".join((y, m, d))