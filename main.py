from utils import parse_settings, speak, listen, randint
from speech_recognition import UnknownValueError, RequestError
import random
import time

settings = parse_settings()

while True:
  a = randint(settings["digit_count"])
  operation = random.choice(settings["operations"])
  b = randint(settings["digit_count"])
  if operation == "-" and b > a:
    expression = f"{b} - {a}"
  else:
    expression = f"{a} {operation} {b}"
  # print(expression)
  speak(expression)
  time.sleep(settings["waiting_time"])
  speak("تفضل")
  while True:
    try:
      c = listen()
    except UnknownValueError:
      speak("آسف، لم أفهم ما قلت!")
      continue
    except RequestError:
      speak("آسف، حدث خطأ تقني!")
      continue
    if not c.isdigit() and not "لا اعرف":
      speak("مدخل خاطئ. برجاء إدخال رقم.")
      continue
    else:
      break
  res = eval(expression)
  if c == "لا اعرف":
    speak(f"لا مشكلة، الإجابة هي {res}")
  elif res == int(c):
    speak("صحيح")
  else:
    speak(f"خطأ. الإجابة الصحيحة هي {res}")
