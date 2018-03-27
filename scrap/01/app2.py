import requests

r = requests.get('https://hinaboshi.com/')

r.encoding = 'utf-8'


print(r.text)