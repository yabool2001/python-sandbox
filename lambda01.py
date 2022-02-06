

from datetime import date, datetime

time_up = lambda s: datetime.utcnow() + datetime.timedelta ( s )


while (1):
    print ( time_up(1) )
