import pyttsx3
import datetime
import calendar
import speech_recognition as sr
import webbrowser
import psutil
import GPUtil
import wmi
import re
import subprocess
import cpuinfo
import os
import platform
import os
import sys
import pyuac
import time
import sqlite3
import pywin32_system32
import pywin32_testutil
import pywintypes
import pywin32_bootstrap
import pywin
from gtts import gTTS
import playsound
from datetime import date





#voices = engine.getProperty('voices')engine.setProperty('voice', voices[ENTER VOICE NUMBER].id)//voice change option

# Connect to the SQLite database
conn = sqlite3.connect("cpu_temp.db")
cur=conn.cursor()




def assistantResponse(text):
    print(text)
    engine.getProperty("voices")
    engine.setProperty("voice", 'tr-tr-m1')
    engine.say(text)
    engine.runAndWait()


def recordAudio():

    r = sr.Recognizer()


    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)


    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:  # Checking for unknown errors
        print('Google Speech Recognition could not understand the audio')
    except sr.RequestError as c:
        print('Request results from Google Speech Recognition service error')

    return data


def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    if (weekday=='Monday'):
        weekday =='Pazartesi'
    elif (weekday=='Tuesday'):
        weekday =='Salı'
    elif weekday=='Wednesday':
        weekday =='Çarşamba'
    elif weekday=='Thursday':
        weekday =='Perşembe'
    elif (weekday =='Friday'):
        weekday =='Cuma'
    elif weekday=='Saturday':
        weekday =='Cumartesi'
    else:
        weekday == 'Pazar'
    monthNum = now.month
    dayNum = now.day
    today=date.today()

    dayofweek=date(today.year,today.month,today.day).weekday()
    #print(dayofweek)

    day_names=['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    ay_adı = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim',
                   'Kasım', 'Aralık']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th','14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    ayıngünleri = ['bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz', 'on', 'onbir', 'oniki', 'onüç','ondört', 'onbeş', 'onaltı', 'onyedi', 'onsekiz', 'ondokuz', 'yirmi', 'yirmibir', 'yirmiiki', 'yirmiüç', 'yirmidört', 'yirmibeş', 'yirmialtı', 'yirmiyedi', 'yirmisekiz', 'yirmidokuz', 'otuz', 'otuzbir']
    assistantResponse('Bugün ' +day_names[dayofweek]   + ', ' + ay_adı[monthNum - 1] + ' the ' + ayıngünleri[dayNum - 1])


def start():
    # ==== Wish Start
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        wish = "Good Morning!"
    elif hour >= 12 and hour < 18:
        wish = "Good Afternoon!"
    else:
        wish = "Good Evening!"
    assistantResponse('Hello Sir,' + wish + ' I am your voice assistant. Please tell me how may I help you')


def tellTime():

        # This method will give the time
        time = str(datetime.datetime.now())

        # the time will be displayed like
        # this "2020-06-05 17:50:14.582630"
        # nd then after slicing we can get time
        print(time)
        hour = time[11:13]
        min = time[14:16]
        assistantResponse("The time is sir " + hour + " Hours and " + min + " Minutes")




def get_audio():
    audio=sr.Microphone()
    recognizer=sr.Recognizer()




def print_hi(name):

    print(f'Hi, {name} this is intern project',)



def display_usage():
    memory_usage=psutil.virtual_memory()
    cpu_usage=psutil.cpu_percent()
    print(f"CPU usage:{cpu_usage}")
    print(f"RAM Memory usage:%{memory_usage[2]}")

    return cpu_usage

def disk_usage():
    disk_info = psutil.disk_usage("/")
    print(f"Total Disk Memory: {disk_info.total / 1024 / 1024 / 1024:.2f} GB")
    print(f"Used Disk Memory: {disk_info.used / 1024 / 1024 / 1024:.2f} GB")
    print(f"Free Disk Memory: {disk_info.free / 1024 / 1024 / 1024:.2f} GB")
    diskusagepercent=disk_info.used/disk_info.total
    diskusagepercent=100*diskusagepercent
    diskusagepercentfirst3number=round(diskusagepercent,2)


    return diskusagepercentfirst3number

def cpu_info():

    cpubigi=cpuinfo.get_cpu_info()
    print(cpubigi)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def cpu_temp():

    w = wmi.WMI(namespace="root\\wmi",privileges=["Security"])
    temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
    print(f"Current temperature: {temperature_info.CurrentTemperature / 10.0-273.15}°C")
    twodecfloatcputemp=round(temperature_info.CurrentTemperature/10.0-273.15,2)
    return twodecfloatcputemp


#def cpu_temp2():
 #   cpu_sensors = wmi.WMI()
 #   cpu_temperature = cpu_sensors.query("SELECT * FROM Win32_Sensor WHERE SensorType='Temperature' AND SensorCategory='Processor'")
 #   print(cpu_temperature[0]['CurrentReading'] / 10.0)






def gpu_usage():
    gpu=GPUtil.getGPUs()[0]
    print(f"GPU temp:{gpu.temperature}'C")
    return gpu.temperature



def op_system():
    print(f"Operating System:{platform.system()}-Release:{platform.release()}-Version:{platform.version()}\nprocessor:{platform.uname().processor}")
    return platform.system()

def ram_usage():
    # Getting % usage of virtual_memory ( 3rd field)
    print('RAM memory % used:', psutil.virtual_memory()[2])
    # Getting usage of virtual_memory in GB ( 4th field)
    print('RAM Used (GB):', psutil.virtual_memory()[3] / 1000000000)
    return psutil.virtual_memory()[2]



def create_table():
    # Create a table
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS pcutility(time float, cputemp float,gputemp float,ramusage float,cpusage,float  diskusage)")

def add_column_table():
    # Add a new column to pcutility table
    new_column = "ALTER TABLE pcutility ADD COLUMN os_version CHAR(25)"
    cur=conn.cursor()
    cur.execute(new_column)

def drop_column_table():
    drop_column = "ALTER TABLE pcutility DROP COLUMN os "
    cur = conn.cursor()
    cur.execute(drop_column)


def speak(text):
    tts=gTTS(text=text,lang="en")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    speak("hello friend")


def get_fps():

    start_time = time.time()
    x = 3  # displays the frame rate every 3 second
    counter = 0
    while True:

        ########################
        # your fancy code here #
        ########################

        counter += 1
        if (time.time() - start_time) > x:
            print("FPS: ", counter / (time.time() - start_time))
            counter = 0
            start_time = time.time()
            break


if __name__ == "__main__":
    while True:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty("voice", voices[1].id)#ingilizce erkek sesi
        #engine.setProperty("voice", voices[2].id)  # ingilizce kadın sesi
       #engine.setProperty("voice", "tr-TR Male")
        engine.setProperty('rate', 150)  # ses hızlandırma-yavaşlatma

        print("Re-launching as admin!")
        #speak("hello friend")
        print_hi('PyCharm')
        assistantResponse("selam")
        getDate()
        tellTime()
        start()
        display_usage()
        assistantResponse(f"ram usage {ram_usage()}percent")
        assistantResponse(f"gpu sıcaklığı{gpu_usage()} celcius")
        cpu_info()
        op_system()
        assistantResponse(f"cpu sıcaklığı {cpu_temp()} celcius")
        get_fps()
        create_table()
        cur.execute("INSERT INTO pcutility VALUES (?, ?,?,?,?,?)", (datetime.datetime.now(), cpu_temp(),gpu_usage(),ram_usage(),display_usage(),disk_usage()))
        #add_column_table()
        #drop_column_table()
        conn.commit()
        time.sleep(30)
    #else:
    #    main()  # Already an admin here.






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
