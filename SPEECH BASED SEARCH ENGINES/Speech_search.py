import speech_recognition as sr
import requests
from bs4 import BeautifulSoup

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your search query:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError:
        print("Error with the request")
    
def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("h3")
    for idx, result in enumerate(results[:5]):
        print(f"{idx+1}. {result.text}")

if __name__ == "__main__":
    query = get_audio()
    if query:
        search_web(query)
