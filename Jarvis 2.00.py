# आवश्यक लाइब्रेरी आयात
import pyttsx3
import datetime
import speech_recognition as sr
import requests
import pyautogui
import webbrowser as वेब_ब्राउजर
import os
import time as समय
import psutil
from newsapi import NewsApiClient
from googletrans import Translator

# एपीआई कुंजियां
एपीआई_कुंजी = {
    "मौसम": "498d13ca5b677e51759b95241a619a02",
    "समाचार": "285e1bfa14de492c86eac4a534e30d1f"
}

# आवाज इंजन सेटअप
वाणी_इंजन = pyttsx3.init()
आवाजें = वाणी_इंजन.getProperty('voices')
वाणी_इंजन.setProperty('voice', आवाजें[1].id)
वाणी_इंजन.setProperty('rate', 170)

def बोलो(पाठ):
    """टेक्स्ट को आवाज में बदलने का फंक्शन"""
    try:
        print(f"जार्विस: {पाठ}")
        वाणी_इंजन.say(पाठ)
        वाणी_इंजन.runAndWait()
    except Exception as त्रुटि:
        print(f"बोलने में त्रुटि: {त्रुटि}")

def सुनो():
    """माइक्रोफोन से आवाज सुनने का फंक्शन"""
    श्रवण = sr.Recognizer()
    try:
        with sr.Microphone() as स्रोत:
            print("सुन रहा हूं...")
            श्रवण.pause_threshold = 1
            श्रवण.energy_threshold = 300
            श्रवण.adjust_for_ambient_noise(स्रोत, duration=0.5)
            ऑडियो = श्रवण.listen(स्रोत)
            print("पहचान रहा हूं...")
            वाक्य = श्रवण.recognize_google(ऑडियो, language="hi-IN")
            print(f"आपने कहा: {वाक्य}")
            return वाक्य.lower()
    except sr.UnknownValueError:
        बोलो("मैं समझ नहीं पाया, कृपया दोबारा बोलें")
        return "कुछ_नहीं"
    except sr.RequestError:
        बोलो("नेटवर्क में समस्या है")
        return "कुछ_नहीं"
    except Exception as त्रुटि:
        print(f"त्रुटि आई है: {त्रुटि}")
        return "कुछ_नहीं"

def समय_बताओ():
    """वर्तमान समय बताने का फंक्शन"""
    try:
        वर्तमान_समय = datetime.datetime.now().strftime("%H:%M")
        बोलो(f"अभी का समय है {वर्तमान_समय}")
    except Exception as त्रुटि:
        बोलो("समय बताने में समस्या आई है")
        print(f"त्रुटि: {त्रुटि}")

def दिनांक_बताओ():
    """वर्तमान दिनांक बताने का फंक्शन"""
    try:
        आज = datetime.datetime.now()
        महीने = ['जनवरी', 'फरवरी', 'मार्च', 'अप्रैल', 'मई', 'जून', 
                'जुलाई', 'अगस्त', 'सितंबर', 'अक्टूबर', 'नवंबर', 'दिसंबर']
        दिन = ['सोमवार', 'मंगलवार', 'बुधवार', 'गुरुवार', 'शुक्रवार', 'शनिवार', 'रविवार']
        
        बोलो(f"आज {दिन[आज.weekday()]}, {आज.day} {महीने[आज.month-1]} {आज.year} है")
    except Exception as त्रुटि:
        बोलो("दिनांक बताने में समस्या आई है")
        print(f"त्रुटि: {त्रुटि}")

def मौसम_बताओ():
    """मौसम की जानकारी बताने का फंक्शन"""
    try:
        बोलो("किस शहर का मौसम जानना चाहते हैं?")
        शहर = सुनो()
        
        if शहर != "कुछ_नहीं":
            यूआरएल = f"http://api.openweathermap.org/data/2.5/weather?q={शहर}&appid={एपीआई_कुंजी['मौसम']}&units=metric&lang=hi"
            जवाब = requests.get(यूआरएल)
            डेटा = जवाब.json()
            
            if जवाब.status_code == 200:
                तापमान = डेटा['main']['temp']
                आद्रता = डेटा['main']['humidity']
                विवरण = डेटा['weather'][0]['description']
                
                बोलो(f"{शहर} में तापमान {तापमान:.1f} डिग्री सेल्सियस है")
                बोलो(f"आद्रता {आद्रता} प्रतिशत है")
                बोलो(f"मौसम {विवरण} है")
            else:
                बोलो("यह शहर नहीं मिला")
    except Exception as त्रुटि:
        बोलो("मौसम की जानकारी प्राप्त करने में समस्या आई")
        print(f"त्रुटि: {त्रुटि}")

def स्क्रीनशॉट_लो():
    """स्क्रीनशॉट लेने का फंक्शन"""
    try:
        बोलो("स्क्रीनशॉट ले रहा हूं")
        स्क्रीनशॉट_समय = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        फाइल_नाम = f'स्क्रीनशॉट_{स्क्रीनशॉट_समय}.png'
        pyautogui.screenshot(फाइल_नाम)
        बोलो("स्क्रीनशॉट सेव हो गया है")
    except Exception as त्रुटि:
        बोलो("स्क्रीनशॉट लेने में समस्या आई")
        print(f"त्रुटि: {त्रुटि}")

def नोट_लिखो():
    """नोट लिखने का फंक्शन"""
    try:
        बोलो("क्या लिखना है, बोलिए")
        नोट_पाठ = सुनो()
        
        if नोट_पाठ != "कुछ_नहीं":
            नोट_समय = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            फाइल_नाम = f"नोट_{नोट_समय}.txt"
            
            with open(फाइल_नाम, 'w', encoding='utf-8') as फाइल:
                फाइल.write(नोट_पाठ)
            बोलो("नोट सेव हो गया है")
    except Exception as त्रुटि:
        बोलो("नोट लिखने में समस्या आई")
        print(f"त्रुटि: {त्रुटि}")

def समाचार_सुनाओ():
    """समाचार सुनाने का फंक्शन"""
    try:
        समाचार_एपीआई = NewsApiClient(api_key=एपीआई_कुंजी['समाचार'])
        बोलो("किस विषय के समाचार चाहिए?")
        विषय = सुनो()
        
        if विषय != "कुछ_नहीं":
            समाचार = समाचार_एपीआई.get_top_headlines(q=विषय, language='hi', country='in')
            
            if समाचार['totalResults'] > 0:
                for क्रम, लेख in enumerate(समाचार['articles'][:5], 1):
                    बोलो(f"समाचार {क्रम}: {लेख['title']}")
                    if क्रम < 5:
                        बोलो("अगला समाचार सुनने के लिए हाँ कहें, रोकने के लिए रुको कहें")
                        जवाब = सुनो()
                        if 'रुको' in जवाब:
                            break
            else:
                बोलो("इस विषय पर कोई समाचार नहीं मिला")
    except Exception as त्रुटि:
        बोलो("समाचार प्राप्त करने में समस्या आई")
        print(f"त्रुटि: {त्रुटि}")

def सिस्टम_जानकारी():
    """सिस्टम की जानकारी बताने का फंक्शन"""
    try:
        सीपीयू = psutil.cpu_percent()
        रैम = psutil.virtual_memory().percent
        बोलो(f"सीपीयू का उपयोग {सीपीयू} प्रतिशत है")
        बोलो(f"रैम का उपयोग {रैम} प्रतिशत है")
    except Exception as त्रुटि:
        बोलो("सिस्टम की जानकारी प्राप्त करने में समस्या आई")
        print(f"त्रुटि: {त्रुटि}")

def अभिवादन():
    """समय के अनुसार अभिवादन"""
    try:
        घंटा = datetime.datetime.now().hour
        if 4 <= घंटा < 12:
            बोलो("सुप्रभात!")
        elif 12 <= घंटा < 16:
            बोलो("शुभ दोपहर!")
        elif 16 <= घंटा < 20:
            बोलो("शुभ संध्या!")
        else:
            बोलो("शुभ रात्रि!")
    except Exception as त्रुटि:
        print(f"अभिवादन में त्रुटि: {त्रुटि}")

def मुख्य():
    """मुख्य कार्यक्रम"""
    try:
        बोलो("नमस्कार! मैं जार्विस हूं")
        अभिवादन()
        
        while True:
            आदेश = सुनो()
            
            if आदेश == "कुछ_नहीं":
                continue
                
            # आदेशों का प्रोसेसिंग
            if 'समय' in आदेश:
                समय_बताओ()
            
            elif 'दिनांक' in आदेश or 'तारीख' in आदेश:
                दिनांक_बताओ()
            
            elif 'मौसम' in आदेश:
                मौसम_बताओ()
            
            elif 'समाचार' in आदेश or 'खबर' in आदेश:
                समाचार_सुनाओ()
            
            elif 'स्क्रीनशॉट' in आदेश:
                स्क्रीनशॉट_लो()
            
            elif 'नोट' in आदेश:
                नोट_लिखो()
            
            elif 'सिस्टम' in आदेश:
                सिस्टम_जानकारी()
            
            elif 'बंद' in आदेश or 'बाय' in आदेश:
                बोलो("जार्विस बंद हो रहा है। फिर मिलेंगे!")
                break
                
    except Exception as त्रुटि:
        print(f"मुख्य कार्यक्रम में त्रुटि: {त्रुटि}")
        बोलो("कोई समस्या आई है, कृपया दोबारा प्रयास करें")

if __name__ == "__main__":
    मुख्य()
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
                    




