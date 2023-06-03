# Calcular dados de uma página a partir do html

from urllib.request import urlopen, Request
from html.parser import HTMLParser


class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.n_worlds = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            for attr in attrs:
                if ((attr[0] == 'class' and attr[1] == 'Odd') or (attr[0] == 'class' and attr[1] == 'Even')):
                    self.n_worlds += 1

    def num_worlds(self):
        return self.n_worlds


def getSource(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url=url, headers=headers)
    html = urlopen(req).read()
    return html.decode()


html = getSource("https://www.tibia.com/community/?subtopic=worlds")
parser = MyParser()
parser.feed(html)
print("There are", parser.num_worlds(), "Worlds in Tibia.")
