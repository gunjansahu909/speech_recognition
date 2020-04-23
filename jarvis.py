import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello sir i am Alexa how may i help you")   
def takeCommand():
    """it takes microphone input from user return string output
    """

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listeining.......")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")


    except Exception as e:
        # print(e)

        print("say that again please...")
        return "None"

    return query    


if __name__== "__main__":
    wishme()
    # while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia......')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")



        elif 'play movies' in query:
            movie_dir = 'E:\\movies'


        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")

        
        


        # elif 'email to gunjan' as query:
        #     try:
        #         speak("what should i say")
        #         content = takeCommand()
        #         to = "gunjansahu909@gmail.com"
        #         sendEmail(to,content)
        #         speak("email is sent")
        #     except Exceptiona as e:
        #         print(e)

            
                









