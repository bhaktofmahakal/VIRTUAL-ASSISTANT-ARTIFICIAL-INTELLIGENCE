# आवश्यक लाइब्रेरी आयात
from gtts import gTTS
import pygame
import os
import datetime
import speech_recognition as sr
import requests
import pyautogui
import webbrowser as वेब_ब्राउजर
import time as समय
import psutil
from newsapi import NewsApiClient
import tempfile
import uuid

# एपीआई कुंजियां
एपीआई_कुंजी = {
    "मौसम": "498d13ca5b677e51759b95241a619a02",
    "समाचार": "285e1bfa14de492c86eac4a534e30d1f"
}

# pygame को इनिशियलाइज़ करें
pygame.mixer.init()

def बोलो(पाठ):
    """टेक्स्ट को आवाज में बदलने का फंक्शन (gTTS का उपयोग करके)"""
    try:
        print(f"जार्विस: {पाठ}")
        
        # अस्थायी फ़ाइल का नाम बनाएं
        temp_dir = tempfile.gettempdir()
        temp_filename = os.path.join(temp_dir, f"jarvis_speech_{uuid.uuid4()}.mp3")
        
        # gTTS का उपयोग करके टेक्स्ट से ऑडियो बनाएं
        tts = gTTS(text=पाठ, lang='hi', slow=False)
        tts.save(temp_filename)
        
        # pygame का उपयोग करके ऑडियो चलाएं
        pygame.mixer.music.load(temp_filename)
        pygame.mixer.music.play()
        
        # ऑडियो के पूरा होने का इंतज़ार करें
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        # अस्थायी फ़ाइल को हटाएं
        try:
            os.remove(temp_filename)
        except:
            pass
            
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

def वेबसाइट_खोलो():
    """वेबसाइट खोलने का फंक्शन"""
    try:
        बोलो("कौन सी वेबसाइट खोलनी है?")
        साइट = सुनो()
        
        if साइट != "कुछ_नहीं":
            if "." not in साइट:
                साइट = साइट + ".com"
            वेब_ब्राउजर.open("https://" + साइट)
            बोलो(f"{साइट} खोल रहा हूं")
    except Exception as त्रुटि:
        बोलो("वेबसाइट खोलने में समस्या आई")
        print(f"त्रुटि: {त्रुटि}")

def वेब_खोज():
    """वेब पर खोज करने का फंक्शन"""
    try:
        बोलो("क्या खोजना चाहते हैं?")
        खोज = सुनो()
        
        if खोज != "कुछ_नहीं":
            यूआरएल = f"https://www.google.com/search?q={खोज}"
            वेब_ब्राउजर.open(यूआरएल)
            बोलो(f"{खोज} के लिए खोज परिणाम यहां हैं")
    except Exception as त्रुटि:
        बोलो("खोज में समस्या आई")
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
                
            elif 'खोलो' in आदेश and ('वेबसाइट' in आदेश or 'साइट' in आदेश):
                वेबसाइट_खोलो()
                
            elif 'खोज' in आदेश or 'सर्च' in आदेश:
                वेब_खोज()
            
            elif 'बंद' in आदेश or 'बाय' in आदेश:
                बोलो("जार्विस बंद हो रहा है। फिर मिलेंगे!")
                break
                
    except Exception as त्रुटि:
        print(f"मुख्य कार्यक्रम में त्रुटि: {त्रुटि}")
        बोलो("कोई समस्या आई है, कृपया दोबारा प्रयास करें")

if __name__ == "__main__":
    मुख्य()