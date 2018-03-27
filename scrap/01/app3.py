import requests

r = requests.get('https://hinaboshi.com')
with open('hinaboshi.html','wb') as f:
    f.write(r.content)


# Write binary
url_file = 'https://hinaboshi.com/rup/rupprakopwalidet/1460321927319907.jpg'
chue_file = 'tapris.jpg'
r = requests.get(url_file)
with open(chue_file,'wb') as f:
    f.write(r.content)



