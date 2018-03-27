import requests
from bs4 import BeautifulSoup

url_naweb = 'https://hinaboshi.com/súpđẹp.html'
r = requests.get(url_naweb)
r.encoding = 'utf-8' # กำหนด encoding กันปัญหาการถอดรหัสผิดแบบ
sup = BeautifulSoup(r.text,'lxml')
print(type(sup))