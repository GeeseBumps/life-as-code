import time


def code():
    """
    Write some codes.
    """
    pass

def workout():
    """
    Some push-ups and running. 
    """
    pass

def day_off():
    """
    Get enough sleep
    """
    time.sleep(60*60*24)

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
for day in days:
    if day in ['SAT', 'SUN']:
        day_off()
    else:
        code()
        workout()

