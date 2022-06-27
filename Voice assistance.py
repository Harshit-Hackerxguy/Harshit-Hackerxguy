import pyttsx3
import wikipedia

# let name of our assistance will be 'bhai'

bhai = pyttsx3.init()
voices = bhai.getProperty('voices')
bhai.setProperty('voice', voices[1].id)
bhai.setProperty('rate', 185)

print("****************************WIKKIPEDIA/GOOGLE******************************")


In = input("Search Wikipedia/Google: ")
Input = input("In how many lines you want your result: ")
result = wikipedia.summary(In, sentences = Input)
bhai.say("According to wikipedia")
print(result)
bhai.say(result)
bhai.say("Thank you for using me")
bhai.runAndWait()