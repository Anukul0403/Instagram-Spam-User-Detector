from bs4 import BeautifulSoup
import requests

req = requests.get("https://www.instagram.com/_its_mahi_babe/")

soup =  BeautifulSoup(req.content,"html.parser")

res = soup.title

print(res.prettify())