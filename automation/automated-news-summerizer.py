from bs4 import BeautifulSoup
import requests 

def getOnlyText(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = " ".join(map(lambda p: p.text, soup.find_all('p')))
    title = " ".join(soup.title.stripped_strings)
    return title, text

news = getOnlyText('https://www.standardmedia.co.ke/thenairobian/news/2001478095/anerlisa-muigai-i-have-been-celibate-for-seven-months')
print('Title : ' + news[0]) 
print("Summary : " + news[1])
