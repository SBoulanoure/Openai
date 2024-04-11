import openai

openai.api_key = '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' # your API key here 
print("Welcome to the chatbot (type exit or bye to exit) ")
while True: 
    message = input("you : ")
    
    # # if the user talk record the message and send it to the chatbot 
    # import speech_recognition as sr

    # # Create a recognizer instance
    # r = sr.Recognizer()

    # # Use the default microphone as the audio source
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     # Record audio
    #     audio = r.listen(source)

    # try:
    #     # Convert the audio to text
    #     message = r.recognize_google(audio)
    #     print("You said: " + message)
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand you")
    # except sr.RequestError as e:
    #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if message == 'exit' or message == 'bye':
        break

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "system", "content": f"{message}" }]
    ) 
    chatResponse = response['choices'][0]['message']['content'] 
    print("chat : " + chatResponse)
    
    #* convert the response to voice of machine 
    import pyttsx3 
    engine = pyttsx3.init() 
    engine.say(chatResponse) 
    engine.runAndWait() 
    engine.stop() 
    
    #* girl voice
#     import pyttsx3

# # Initialize the speech engine
#     engine = pyttsx3.init()

# # Get the list of voices
#     voices = engine.getProperty('voices')

# # Print all available voices

# # Use the first female voice in the voices list
#     for voice in voices:
#         if "Microsoft Zira Desktop - English (United States)" in voice.name:
#             engine.setProperty('voice', voice.id)
#             break

# # The text you want to convert to speech
#     text = chatResponse

# # Use the speech engine to say the text and run the speech engine
#     engine.say(text)
#     engine.runAndWait()