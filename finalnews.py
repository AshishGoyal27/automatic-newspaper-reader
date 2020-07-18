import requests
import json
import webbrowser
from win32com.client import Dispatch
def speak(string):
    '''To speak the particular string '''
    speak = Dispatch('SAPI.spVoice')
    speak.speak(string)

speak("News for today.. Lets begin")
print("News for today.. Lets begin")
print("**************************************************")
url = ('http://newsapi.org/v2/top-headlines?'
        'country=in&'
        'apiKey=yours_api_keys')
data = requests.get(url=url)
india = data.json()
speak("No. of top headlines you want to read")
n = int(input("No. of top headlines you want to read"))
for i in range(n):
    speak("Newspaper name " + india['articles'][i]['source']['name'])
    print(f'{i+1}. Newspaper name: ' + india['articles'][i]['source']['name'])
    speak("Headline of the newspaper is " + india['articles'][i]['title'])
    print("Headline of the newspaper is :\n" + india['articles'][i]['title'])
    speak("To read this article complete, type Y for open it in browser")
    a = input("\nTo read this article complete,type Y for open it in browser \n").lower().strip()
    if(a=='yes' or a=='y'):
        webbrowser.open(india['articles'][i]['url'],new=2)
    print("-----------------------------------------------------------------------")
speak("Thanks for listening...")
print("Thanks for listening...")
print("**************************************************")
