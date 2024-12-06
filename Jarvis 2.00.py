import pyttsx3  # pip install pyttsx3 for text-to-speech functionality
import datetime
import speech_recognition as sr  # 
import smtplib
from email_credentials import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
from nltk.tokenize import word_tokenize

from newvoices import speak
import newvoices


# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[1].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def get_voices():
#     voices = engine.getProperty('voices')
#     print(voices[1].id)
#     try:
#         # voice_choice = int(input(" for working with assisant type 1\n"))
#         if voices == 1:
#             engine.setProperty('voice', voices[1].id)  # Male ai assistant
#             speak("Hello, I am Jarvis.")
#         # elif voice_choice == 2:
#         #     engine.setProperty('voice', voices[1].id)  # Female ai assitant
#         #     speak("Hello, I am Friday.")
#         else:
#             print("Invalid choice, defaulting to male voice.")
#             engine.setProperty('voice', voices[1].id)  
#     except ValueError:
#         print("Invalid input, defaulting to male voice.")
#         engine.setProperty('voice', voices[1].id)  

def get_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")  # hour = I, minutes = M, seconds = S
    speak("The current time is:")
    speak(Time)

def get_date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is:")
    speak(day)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening Sir!")
    else:
        speak("Good night Sir!")

def wishme():
    #  speak("I'm Jarvis, An Advance Virtual Machine with Enhanced Features")
    # get_time()
    # get_date()
    greeting()
    speak("Jarvis At Your Service, Please tell me what can I do for you?")

def takeCommandCMD():
    query = input("Please tell me what can I do for you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('what should i search for')
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q=' + search)



# def news():
#     newsapi = NewsApiClient(api_key='285e1bfa14de492c86eac4a534e30d1f')
#     speak('what topic you need the news about?')
#     topic = takeCommandMic()
#     data = newsapi.get_top_headlines(q = topic,
#                                      language='en',
#                                      page_size=5)

#     newsdata = data['articles']
#     for x,y in enumerate(newsdata):
#         print(f'{x}{y["description"]}')
#         speak((f'{x}{y["description"]}'))

#     speak("that's it for now i'll update you in some time")

# def news():
#     # Initialize the News API client
#     newsapi = NewsApiClient(api_key='285e1bfa14de492c86eac4a534e30d1f')
    
#     # Ask user for the news topic
#     speak('What topic do you need the news about?')
#     topic = takeCommandMic()
    
#     try:
#         # Fetch top headlines for the specified topic
#         data = newsapi.get_top_headlines(q=topic, language='en', page_size=5)
        
#         # Check if articles are returned
#         newsdata = data.get('articles', [])
#         if not newsdata:
#             speak("Sorry, I couldn't find any news on that topic.")
#             return
        
#         # Loop through the articles and read out the description
#         for index, article in enumerate(newsdata, start=1):
#             description = article.get('description', 'No description available')
#             print(f"{index}: {description}")
#             speak(f"{index}: {description}")
        
#         speak("That's it for now. I'll update you again later.")
    
#     except Exception as e:
#         speak("Sorry, there was an error retrieving the news.")
#         print(f"Error: {e}")
def text2speech():
    text =  clipboard.paste()
    print(text)
    speak(text)


def screenshot():
    name_img = tt.time()
    name_img = f'U:\\Projects\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s =[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3)) 
    s.extend(list(s4))

    random.shuffle(s)
    newpass =("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)


def flip():
    speak("okay sir, flipping a coin for you")
    coin = ['heads', 'tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("I flipped the coin and you got" + toss)

def roll():
    speak("okay sir rolling a die for you")
    die = ['1','2','3','4','5','6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("I rolled a die and you got"+ roll)




if __name__ == "__main__":
   speak("Welcome Back Sir!")
  # get_voices()  
   wishme()
#    wakeword = "jarvis"
while True:
     query = takeCommandMic().lower()
    #  query = word_tokenize(query)
    #  print(query)

    #  if wakeword in query:
     if "time" in query:
        get_time()

     elif "date" in query:
            get_date()

     elif "email" in query:
            email_list = {
                'Friday':'vobajej794@ruhtan.com'
            }
            try:
                speak("To whom you want to send the mail?")
                name = takeCommandMic()
                receiver = email_list[name]
                speak("what is the subject of the mail?")
                subject = takeCommandMic()
                speak('what should i say?')
                content = takeCommandMic()
                sendEmail(receiver, subject, content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("unable to send the email")

     elif 'message' in query:
            user_name = {
                'DS': '+91 9554997354'
            }
            try:
                speak("To whom you want to send the whats app message?")
                name = takeCommandMic()
                phone_no = user_name[name]
                speak("what is the message?")
                message = takeCommandMic()
                sendwhatsmsg(phone_no, message)
                speak("message has been send")
            except Exception as e:
                print(e)
                speak("unable to send the message")


     elif 'wikipedia' in query:
            speak("Searching on Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

     elif 'search' in  query:
            searchgoogle()

     elif 'youtube' in query:
            speak('what should i search for on YouTube?')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)


    #  elif 'weather' in query:
    #            city = 'new york'
    #            url = f'http://api.openweathermap.org/datsa/2.5/weather?q={city}&units=imperial&appid={498d13ca5b677e51759b95241a619a02}'    

    #            res = requests.get(url)   
    #            data = res.json()

    #            weather = data['weather'] [0] ['main']
    #            temp = data['main']['temp']
    #            desp = data['weather'] [0] ['description']
    #            print(weather)
    #            print(temp)
    #            print(desp)
    #            speak(f'weather in {city} city is like')
    #            speak('temperature : {} degree celcius'.format(temp))
    #            speak('weather is {}'.format(desp))
    #  elif 'news' in query:
        #        news()
     elif 'read' in query:
        text2speech()

     elif 'docs' in query:
        os.system('explorer C://{}'.format(query.replace('open','')))

     elif 'vs code' in query:
        codepath = 'C:\\Users\\movie\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(codepath)

     elif 'joke' in query:
        speak(pyjokes.get_joke())

     elif 'screenshot' in query:
        screenshot()


     elif 'remember that' in query:
        speak("what should i remember?")
        data = takeCommandMic()
        speak("you said me to remember that "+ data)
        remember = open('data.txt','w')
        remember.write(data)
        remember.close()

     elif 'do you know anything' in query:
        remember = open('data.txt','r')
        speak("i remember you told me that, "+remember.read())

     elif 'password' in query:
        passwordgen()

     elif 'flip' in query:
            flip()

     elif 'roll' in query:
            roll()
            
     elif 'offline' in query:  
        quit()   
                    




