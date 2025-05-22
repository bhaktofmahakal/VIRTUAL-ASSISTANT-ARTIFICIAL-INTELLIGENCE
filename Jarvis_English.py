# Import required libraries
from gtts import gTTS
import pygame
import os
import datetime
import speech_recognition as sr
import requests
import pyautogui
import webbrowser
import time
import psutil
from newsapi import NewsApiClient
import tempfile
import uuid

# API keys
API_KEYS = {
    "weather": "498d13ca5b677e51759b95241a619a02",
    "news": "285e1bfa14de492c86eac4a534e30d1f"
}

# Initialize pygame
pygame.mixer.init()

def speak(text):
    """Function to convert text to speech using gTTS"""
    try:
        print(f"Jarvis: {text}")
        
        # Create temporary file name
        temp_dir = tempfile.gettempdir()
        temp_filename = os.path.join(temp_dir, f"jarvis_speech_{uuid.uuid4()}.mp3")
        
        # Create audio from text using gTTS
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(temp_filename)
        
        # Play audio using pygame
        pygame.mixer.music.load(temp_filename)
        pygame.mixer.music.play()
        
        # Wait for audio to complete
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        # Remove temporary file
        try:
            os.remove(temp_filename)
        except:
            pass
            
    except Exception as error:
        print(f"Error in speaking: {error}")

def listen():
    """Function to listen from microphone"""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            recognizer.energy_threshold = 300
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)
            print("Recognizing...")
            sentence = recognizer.recognize_google(audio, language="en-US")
            print(f"You said: {sentence}")
            return sentence.lower()
    except sr.UnknownValueError:
        speak("I didn't understand, please speak again")
        return "nothing"
    except sr.RequestError:
        speak("There's a problem with the network")
        return "nothing"
    except Exception as error:
        print(f"Error occurred: {error}")
        return "nothing"

def tell_time():
    """Function to tell current time"""
    try:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    except Exception as error:
        speak("There was a problem telling the time")
        print(f"Error: {error}")

def tell_date():
    """Function to tell current date"""
    try:
        today = datetime.datetime.now()
        months = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        speak(f"Today is {days[today.weekday()]}, {months[today.month-1]} {today.day}, {today.year}")
    except Exception as error:
        speak("There was a problem telling the date")
        print(f"Error: {error}")

def tell_weather():
    """Function to tell weather information"""
    try:
        speak("Which city's weather would you like to know?")
        city = listen()
        
        if city != "nothing":
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEYS['weather']}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                description = data['weather'][0]['description']
                
                speak(f"The temperature in {city} is {temperature:.1f} degrees Celsius")
                speak(f"The humidity is {humidity} percent")
                speak(f"The weather is {description}")
            else:
                speak("City not found")
    except Exception as error:
        speak("There was a problem getting weather information")
        print(f"Error: {error}")

def take_screenshot():
    """Function to take screenshot"""
    try:
        speak("Taking screenshot")
        screenshot_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f'screenshot_{screenshot_time}.png'
        pyautogui.screenshot(file_name)
        speak("Screenshot saved")
    except Exception as error:
        speak("There was a problem taking the screenshot")
        print(f"Error: {error}")

def write_note():
    """Function to write a note"""
    try:
        speak("What would you like me to write?")
        note_text = listen()
        
        if note_text != "nothing":
            note_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"note_{note_time}.txt"
            
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(note_text)
            speak("Note saved")
    except Exception as error:
        speak("There was a problem writing the note")
        print(f"Error: {error}")

def tell_news():
    """Function to tell news"""
    try:
        news_api = NewsApiClient(api_key=API_KEYS['news'])
        speak("What topic would you like to hear news about?")
        topic = listen()
        
        if topic != "nothing":
            news = news_api.get_top_headlines(q=topic, language='en', country='us')
            
            if news['totalResults'] > 0:
                for index, article in enumerate(news['articles'][:5], 1):
                    speak(f"News {index}: {article['title']}")
                    if index < 5:
                        speak("Say yes to hear the next news, or stop to end")
                        response = listen()
                        if 'stop' in response:
                            break
            else:
                speak("No news found on this topic")
    except Exception as error:
        speak("There was a problem getting the news")
        print(f"Error: {error}")

def system_info():
    """Function to tell system information"""
    try:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        speak(f"CPU usage is {cpu} percent")
        speak(f"RAM usage is {ram} percent")
    except Exception as error:
        speak("There was a problem getting system information")
        print(f"Error: {error}")

def greeting():
    """Greeting based on time"""
    try:
        hour = datetime.datetime.now().hour
        if 4 <= hour < 12:
            speak("Good morning!")
        elif 12 <= hour < 16:
            speak("Good afternoon!")
        elif 16 <= hour < 20:
            speak("Good evening!")
        else:
            speak("Good night!")
    except Exception as error:
        print(f"Error in greeting: {error}")

def open_website():
    """Function to open websites"""
    try:
        speak("Which website would you like to open?")
        site = listen()
        
        if site != "nothing":
            if "." not in site:
                site = site + ".com"
            webbrowser.open("https://" + site)
            speak(f"Opening {site}")
    except Exception as error:
        speak("There was a problem opening the website")
        print(f"Error: {error}")

def search_web():
    """Function to search the web"""
    try:
        speak("What would you like to search for?")
        query = listen()
        
        if query != "nothing":
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
    except Exception as error:
        speak("There was a problem with the search")
        print(f"Error: {error}")

def main():
    """Main program"""
    try:
        speak("Hello! I am Jarvis")
        greeting()
        
        while True:
            command = listen()
            
            if command == "nothing":
                continue
                
            # Processing commands
            if 'time' in command:
                tell_time()
            
            elif 'date' in command:
                tell_date()
            
            elif 'weather' in command:
                tell_weather()
            
            elif 'news' in command:
                tell_news()
            
            elif 'screenshot' in command:
                take_screenshot()
            
            elif 'note' in command:
                write_note()
            
            elif 'system' in command:
                system_info()
                
            elif 'open' in command and 'website' in command:
                open_website()
                
            elif 'search' in command:
                search_web()
            
            elif 'exit' in command or 'bye' in command or 'quit' in command:
                speak("Jarvis shutting down. Goodbye!")
                break
                
    except Exception as error:
        print(f"Error in main program: {error}")
        speak("There was a problem, please try again")

if __name__ == "__main__":
    main()