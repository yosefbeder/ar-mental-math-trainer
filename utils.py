import sys
import random
import pygame
from gtts import gTTS
import io
import speech_recognition as sr

def parse_settings():
  return {
    "operations": list(sys.argv[1].replace("x", "*")),
    "digit_count": int(sys.argv[2]),
    "waiting_time": int(sys.argv[3]),
  }

def randint(digit_count):
  return random.randint(10**(digit_count - 1), 10**digit_count - 1)

def speak(text, lang='ar'):
    pygame.mixer.init()

    audio_data = io.BytesIO()
    
    tts = gTTS(text=text.replace("-", "ناقص").replace("*", "ضرب"), lang=lang)
    tts.write_to_fp(audio_data)
    
    audio_data.seek(0)
    
    pygame.mixer.music.load(audio_data, 'mp3')
    
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

recognizer = sr.Recognizer()

def listen():
  with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
  return recognizer.recognize_google(audio, language="ar-SA")
