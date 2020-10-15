import speech_recognition as sr  
r = sr.Recognizer()  

a = int(input("1.Audio file or 2.Mic\n"))

if a==1 :
   
    with sr.AudioFile(input("Enter file path\n")) as source:
    
        audio_text = r.listen(source)
    
        try:
        
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)
     
        except:
            print('Sorry.. run again...')
        
else:        
    with sr.Microphone() as source:  
        print("Speak Anything :")  
        audio = r.listen(source)  
    
    
        try:  
            text = r.recognize_google(audio)  
            print("You said : {}".format(text))  


        except:  
            print("Sorry could not recognize what you said") 