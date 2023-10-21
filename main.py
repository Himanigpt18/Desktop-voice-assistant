import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import time
import pyautogui
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from PyMails import *
import encoders
import instadownloader


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voices[0]id)
engine.setProperty('voices', voice[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3,phrase_time_limit=5)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        speak(f"good morning, its {tt}")
    elif hour>12 and hour<18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("It's tillu here. please tell me how can i help you")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()
#to send email
def news(): 
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=ecb0f8ec47ff4e8b835ca67419ae193c"

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        # "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return "The current location is ", location_data



if __name__ == "__main__":
    wish()
    while True:
    #if 1:
        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('camera', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()


        elif "play music" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,rd))

        elif "ip address" in query:
           ip = get('https://api.ipify.org').text
           speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query or "google" in query:
            speak("sir,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+919013152579", "this is testing protocol",1,12)

        elif "play song on youtube" in query or "play song" in query:
            speak("which song do you want to listen?")
            x = takecommand().lower()
            kit.playonyt(x)

        elif "email to tanya" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "tanya122c@gmail.com"
                sendEmail(to,content)
                speak("email has been sent to tanya")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to tanya")

        elif "no thanks" in query:
            speak("thanks for using me sir,have a good day.")
            sys.exit()

    # to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

    # to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

    #to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()
    # Email queries
        elif "email to tanya" in query:
            speak("what would you like to say?")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'heemani2001@gmail.com'  # your email id
                password = '*********'  # your gmail password
                send_to_email = 'tanya122c@gmail.com'  # email id whom mail is to be sent
                speak("what is the subject for this email?")
                query = takecommand().lower()
                subject = query  # the subject in the email being sent
                speak("what message do you want to send?")
                query2 = takecommand().lower()
                message = query2  # message being sent in this email
                speak("please attach the correct path of the file tht you want to attach")
                file_location = input("Please enter the path here: ")  # file is being feached by the input path
                speak("Please wait, Your mail is being sent")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))

                # setup for the attached file
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)

                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                # attach the attachment to the MIMEMultipart objet
                msg.attach(part)
                server = smtplib.SMTP('smtp@gmail.com', 587)  # connect to the server
                server.starttls()  # use TLS
                server.login(email, password)  # login to the email server
                server.sendmail(email, send_to_email, message)  # send the email
                server.quit()  # logout from the email server
                speak("Email has been sent to tanya")


            else:
                email = "heemani2001@gmail.com"  # your email id
                password = '*********'  # your gmail password
                send_to_email = 'tanya122c@gmail.com'  # person whom you are sending the email
                message = query  # message in the email

                server = smtplib.SMTP('smtp@gmail.com', 587)  # connect to the server
                server.starttls()  # use TLS
                server.login(email, password)  # login to the email server
                server.sendmail(email, send_to_email, message)  # send the email
                server.quit()  # logout from the email server
                speak("Email has been sent to tanya")


    # to check insta profile ----- NEED TO PROVIDE INSTA INFO
        elif "instagram profile" in query or "show my profile on instagram" in query:
            speak("sir please enter the user name correctly.")
            name = input("enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Here is the profile of the user {name}")
            time.sleep(5)
            speak("Would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instadownloader.InstaDownloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir. Picture is saved in our folder")
            else:
                exit()

    # to take screenshot-----SAVES THE SCREENSHOT IN PROJECT FOLDER
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir,please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("done sir")

            # find my location using ip address------NOT GIVING LOCATION RATHER PROVIDING IP ADDRESS
        elif "where am I" in query or "where are we" in query:
            speak("wait sir,let me check")
            speak(get_location())
            exit()

            # try:
            #    ipAdd = requests.get('https://api.ipify.org').text
            #    print(ipAdd)
            #    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
            #    geo_requests = requests.get(url)
            #    geo_data = geo_requests.json()
            #    #print(geo_data)
            #    city = geo_data['city']
            #    #state = geo_data[state]
            #    country = geo_data['country']
            #    speak(f"sir i am not sure,but i think we are in {city} city of {country} country")
            # finally:
            #    speak("sorry sir, due to network issue i unable to find where we are")



        speak("sir, do you have any other work")
