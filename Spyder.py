#work in progress for now
import urllib.request


link = 'https://en.wikipedia.org/wiki/Gartin'
page = urllib.request.urlopen(link)
decode = page.read().decode('utf-8')

