import pyttsx3
import datetime
import calendar
import speech_recognition as sr
import webbrowser
import psutil
import GPUtil





engine = pyttsx3.init()
#voices = engine.getProperty('voices')engine.setProperty('voice', voices[ENTER VOICE NUMBER].id)//voice change option

def assistantResponse(text):
    print(text)

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
    dayofweek=dayNum%7

    day_names=['Pazar','Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar']

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    ay_adı = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim',
                   'Kasım', 'Aralık']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th','14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    ayıngünleri = ['bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz', 'on', 'onbir', 'oniki', 'onüç','ondört', 'onbeş', 'onaltı', 'onyedi', 'onsekiz', 'ondokuz', 'yirmi', 'yirmibir', 'yirmiiki', 'yirmiüç', 'yirmidört', 'yirmibeş', 'yirmialtı', 'yirmiyedi', 'yirmisekiz', 'yirmidokuz', 'otuz', 'otuzbir']
    assistantResponse('Bugün ' +day_names[dayofweek+1]   + ', ' + ay_adı[monthNum - 1] + ' the ' + ayıngünleri[dayNum - 1])


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
def basla():
    saat = int(datetime.datetime.now().hour)
    if saat >= 0 and saat< 12:
        wish = "Günaydın!"
    elif saat>= 12 and saat < 18:
        wish = "Tünaydın!"
    else:
        wish = "İyi akşamlar!"
    assistantResponse('Merhaba,' + wish + ' Ben sizin sesli asistanınızım. Size nasıl yardımcı olabilirim')

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


def saatisöyle():
    # This method will give the time
    time = str(datetime.datetime.now())

    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    # nd then after slicing we can get time
    print(time)
    saat=str(datetime.datetime.now().hour)
    dakika= str(datetime.datetime.now().minute)

    assistantResponse("Saat" + saat +" i "+ dakika + "geçiyo")
def print_hi(name):

    print(f'Hi, {name} this is intern project',)



def display_usage(cpu_usage,memory_usage):


 print(f"CPU usage:{cpu_usage}")
 print(f"Memory usage:%{memory_usage[2]}")





def gpu_usage():
    gpu=GPUtil.getGPUs()[0]
    print(f"GPU temp:{gpu.temperature}'C")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    assistantResponse("selam")
    getDate()
    tellTime()
    start()
    display_usage(psutil.cpu_percent(),psutil.virtual_memory())
    gpu_usage()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
