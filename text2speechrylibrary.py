
try:
    import pyttsx3
    engine = pyttsx3.init()

    engine.say("hello this is a test.")
    engine.runAndWait()
    
    print('pyttsx3 is imported correctly')

except ImportError:
    print("pyttsx3 is not installed")

except Exception as e:
    print("error occured", e)       
