import speech_recognition
import pyttsx3
from wolframalpha import Client
# make sure to install everything

client = Client('PQKR53-4VJTP72EUK') # API Key
print("What is your question?")

recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()

# Let's calibrate the microphone based on the surroundings:
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)

# Now that it's callibrated, we can listen to the speaker.
# It will automatically stop when you stop talking.
with microphone as source:
    print("Listening...")
    audio = recognizer.listen(source, timeout=2, phrase_time_limit=15)

# Then convert the microphone audio to text
text = recognizer.recognize_google(audio)


# TODO: Get the text answer to the question from Wolfram Alpha
response = client.query(text)
pod = next(response.results)
answer = pod.text # ???
# print("You said: " + text)

print("Your question: {}".format(text))
print("Answer: {}".format(answer))

# And now we can use the `text` variable to do anything we want:

# You only need to create the engine once...
engine = pyttsx3.init()

# ...And then you can use it as many times as you want
engine.say(answer)
engine.runAndWait()