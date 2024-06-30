# today is 1/09/23 about 6am. its my third day doing automation where i have learned the concept of web scraping 
# using X-path to select html tags


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
import sys

#created and formats the current date and time and appends it to the file path 
exePath = os.path.dirname(sys.executable)
date = datetime.now()
mdt = date.strftime('%m%d%Y')

# while the path is not working at this time, the rest of the logic flow is correctly implimented
website = 'https://chromedriver.chromium.org/downloads'
path = 'chromedriver-win64/chromedriver.exe'

# today is 05/09/2023 and after days of debugging i found the reson i recived the Error caused my script
# not to work is because in the newer version of selenium you dont need to specify the path to your
# webdriver its done automatcly
options = Options()
options.headless = True




service = Service(executable_path=path)
driver = webdriver.Chrome(options=options)
driver.get(website)


containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]') 

titles= []
subtitles = []
links = []

for i in containers:
    title= i.find_element(by='xpath', value='./a/h2').text
    subtitle = i.find_element(by='xpath', value='./a/p').text
    link = i.find_element(by='xpath', value='./a').get_attribute('href')

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

import pandas as pd

myDict = {'titles': titles, 'subtitle': subtitles, 'links': links}



headLine = pd.DataFrame(myDict)
fileDir = f'{mdt}hedline.csv'

finalPath = os.path.join(fileDir,exePath)
headLine.to_csv(finalPath)


driver.quit()




