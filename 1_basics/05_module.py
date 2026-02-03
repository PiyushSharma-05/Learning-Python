# import pyjokes

# print("printing jokes....")
# jokes = pyjokes.get_joke()
# print(jokes)
import pyttsx3
engine = pyttsx3.init()

engine.say('''
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.

           Hii I am Piyush And I want to become a Coder

''')
engine.runAndWait()