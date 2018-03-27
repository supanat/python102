from urllib.request import urlopen


html = urlopen('https://hinaboshi.com').read()
#print(html)
print(html.decode('utf-8'))