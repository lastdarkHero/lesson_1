# import speech_recognition as sr

# recognizer = sr.Recognizer()

# while True:
#     with sr.Microphone(device_index=1) as sourse:
#         print("Помурчи в микрофон пж")
#         audio = recognizer.listen(sourse)

#     speech = recognizer.recognize_google(audio, language="ru_RU")  
#     print(f"Вы сказали: {speech}")  

#     if speech.lower() == "привет":
#         print("Дарова")


import speech_recognition as sr
import random

recognizer = sr.Recognizer()

while True:
    with sr.Microphone(device_index=1) as sourse:
        print("Посоветую фильм командой 'Фильм': ")
        audio = recognizer.listen(sourse)

    speech = recognizer.recognize_google(audio, language="ru_RU")  
    print(f"Вы сказали: {speech}")  

    if speech.lower() == "фильм":
        films = ("1+1", "Джентльмены", "Волк с Уолл-стрит", "Брат", "Аватар", "Чебурашка", "Человек-Паук")
        random_films = random.choice(films)
        print("Можешь посмотреть " + random_films)



