# Jarvis Virtual Assistant

## Overview
Jarvis is a virtual assistant that can perform various tasks through voice commands. It supports both Hindi and English languages, making it versatile for different users.

## Features
- **Voice Recognition**: Understands voice commands in both Hindi and English
- **Text-to-Speech**: Responds with natural-sounding voice using Google's TTS service
- **Time and Date**: Tells the current time and date
- **Weather Information**: Provides weather updates for any city
- **News Updates**: Reads the latest news on requested topics
- **Screenshot**: Takes screenshots of your screen
- **Note Taking**: Creates text notes from your voice input
- **System Information**: Reports CPU and RAM usage
- **Web Browsing**: Opens websites and performs web searches

## How to Use
1. **Start the Assistant**:
   - Run `Jarvis_Menu.bat` to choose between Hindi and English versions
   - Or directly run `Start_Jarvis_Hindi.bat` or `Start_Jarvis_English.bat`

2. **Voice Commands**:
   - **English Version**:
     - "What's the time?" - Tells the current time
     - "What's the date today?" - Tells the current date
     - "How's the weather?" - Asks for a city and tells the weather
     - "Tell me the news" - Asks for a topic and reads news
     - "Take a screenshot" - Takes a screenshot
     - "Write a note" - Creates a text note
     - "System information" - Tells CPU and RAM usage
     - "Open website" - Opens a website
     - "Search for..." - Performs a web search
     - "Bye" or "Exit" - Closes the assistant

   - **Hindi Version**:
     - "समय क्या है?" - बताता है वर्तमान समय
     - "आज की तारीख क्या है?" - बताता है वर्तमान दिनांक
     - "मौसम कैसा है?" - शहर पूछता है और मौसम बताता है
     - "समाचार सुनाओ" - विषय पूछता है और समाचार पढ़ता है
     - "स्क्रीनशॉट लो" - स्क्रीनशॉट लेता है
     - "नोट लिखो" - टेक्स्ट नोट बनाता है
     - "सिस्टम जानकारी" - CPU और RAM उपयोग बताता है
     - "वेबसाइट खोलो" - वेबसाइट खोलता है
     - "खोज करो..." - वेब खोज करता है
     - "बंद करो" या "बाय" - असिस्टेंट बंद करता है

## Requirements
- Python 3.12
- Internet connection (for speech recognition, TTS, weather, and news)
- Microphone (for voice commands)

## Dependencies
- gtts (Google Text-to-Speech)
- pygame (for audio playback)
- speech_recognition (for voice recognition)
- requests (for API calls)
- pyautogui (for screenshots)
- psutil (for system information)
- newsapi-python (for news updates)

## Note
This assistant requires an internet connection to function properly as it uses Google's services for speech recognition and text-to-speech conversion.