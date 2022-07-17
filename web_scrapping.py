import requests
from bs4 import BeautifulSoup

user=input("Enter Username\n")
url="https://github.com/"+user
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
profile_img=soup.find('img',{'alt':'Avatar'})['src'] #these are the particular specifications of what actually we are looking for
print(profile_img)