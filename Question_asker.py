import random
import wolframalpha

client = wolframalpha.Client(wolframalpha_api_key)#U will need to get a wolframalpha accese key to use this project.

greeting_words = ['Hello what is your name', 'who are you', 'what are you called by', 'got a name']
location = ['Where are you from', 'Where were you born', 'where are you located']

def greeting_choice():
    greeting_choice = input(random.choice(greeting_words))

    return
def location():
    location_choice = input(random.choice(location))


greeting_choice()
location

facts = input('Whant to hear some facts about the world')
if facts == 'yes':

    question1 = input('Input a question')

    res = client.query(question1)
    print(next(res.results).text)



else:
    print('Ok see you later')
    end()
