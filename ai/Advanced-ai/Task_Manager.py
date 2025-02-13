#Function
import datetime
from Speaking import Say
#2 Types

#1 - Non Input
#eg: Time , Date , Speedtest

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

#2 - Input
#eg - google search , wikipedia

def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)
"""
    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        import pywhatkit
        pywhatkit.search(query)
        
    elif "youtube" in tag:
        query = str(query).replace("youtube","")
        query = query.replace("play","")
        query = query.replace("search","")
        query = query.replace("on","")
        import pywhatkit
        pywhatkit.playonyt(query)
        
    elif "email" in tag:
        def mail(Sender_email, sender_password, receiver_email, msg):
            import smtplib
            try:
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login(sender_email, sender_password)
                mail.snedmail(sender_email, receiver_email, msg)
                mail.close()
                return True
            except Exception as e:
                print(e)
                return false
        mail()
        
    elif "camera" in tag:
        import cv2
        capture_video = cv2.VideoCapture(0)
        if not capture_video.isOpened():
            raise IOError("Cannot open the camera")
            speak("Camera not opening")
        
        while True:
            ret, frame = capture_video.read()
            frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_AREA)
            cv2.imshow('Input', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        capture_video.release()
        cv2.destroyAllWindows()
    
        
    
    elif "Question" in tag:
        from pywikihow import search_wikihow , max_result
        speak("Finding answer")
        op = query.replace("jarvis", "")
        max_result = 1
        how_to_func = search_wikihow(op,max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        speak(how_to_func[0].summary)
    """
