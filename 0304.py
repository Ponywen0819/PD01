def activate():
    print("turn on AC")

def autoCool(temperature:int, wind:int, humidity:int):
    if (temperature > 30) and (wind == 0):
        activate()
    elif (humidity >85):
        activate()
    