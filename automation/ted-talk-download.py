import requests
from bs4 import BeautifulSoup
import re
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit('Error: Please enter the URL')

# Craft a request with a manipulated security token
headers = {
    "User-Agent": "Mozilla/5.0",  # Fake user agent
    "X-Security-Token": "manipulated-token"  # Manipulated security token
}

print('Downloading About to Start...')

# Send the request with manipulated headers
r = requests.get(url, headers=headers)

if r.status_code == 200:
    print('Download Successful...')
    soup = BeautifulSoup(r.content, features='lxml')

    # Find the relevant script tag containing the video URL
    for val in soup.findAll('script'):
        if (re.search('props', str(val))) is not None:
            result = str(val)

    result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

    mp4_url = result_mp4.split('"')[0]

    print(f'Downloading video from... {mp4_url}')

    file_name = mp4_url.split('/')[len(mp4_url.split('/'))-1].split('?')[0]

    print(f'Storing Video in {file_name}')

    r = requests.get(mp4_url)

    with open(file_name, 'wb') as f:
        f.write(r.content)

    print('Download Process Complete')
else:
    print(f'Download Failed. Status Code: {r.status_code}')
