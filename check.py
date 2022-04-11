import psutil, datetime, sqlite3

def cpuPercent():
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    date = now.strftime('%d:%m:%Y')
    return [(f'{date} | {time}', str(psutil.cpu_percent()))]

def memoryPercent():
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    date = now.strftime('%d:%m:%Y')
    return [(f'{date} | {time}', psutil.virtual_memory().percent)]

def temperatureDegrees():
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    date = now.strftime('%d:%m:%Y')
    #return [(f'{date} | {time}', psutil.sensors_temperatures(fahrenheit=False)['cpu_thermal'][0][1])]
    return [(f'{date} | {time}', '50.00')]

def diskUsage():
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    date = now.strftime('%d:%m:%Y')
    return [(f'{date} | {time}', str(psutil.disk_usage('/').percent))]