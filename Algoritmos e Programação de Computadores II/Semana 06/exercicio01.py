# Python WWW API

from urllib.request import urlopen

def getSource(url):
    response = urlopen(url)
    html = response.read()

    return html.decode()

html = getSource("https://g1.globo.com/")
print(html)