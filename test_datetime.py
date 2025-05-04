from datetime import date, datetime, timedelta

# d = date(2025, 5, 3)
# dt = datetime(2025, 5, 3, 16, 36, 00)

d = date.today()
dt = datetime.today()

delta = timedelta(days=5)
date_final = d - delta

date_str = d.strftime("%d %b %y")