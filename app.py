from flask import Flask, render_template
import psutil, datetime

app = Flask(__name__)

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
    return [(f'{date} | {time}', psutil.sensors_temperatures(fahrenheit=False)['cpu_thermal'][0][1])]

@app.route('/')
def index():
    return render_template('index.html', cpu=cpuPercent(), memory=memoryPercent(), temp=temperatureDegrees())

if __name__ == '__main__':
    app.run(debug=True)