import requests
from bs4 import BeautifulSoup

url = 'https://auth.berkeley.edu/cas/login?service=https%3A%2F%2Fshib.berkeley.edu%2Fidp%2FAuthn%2FExternal%3Fconversation%3De2s1%26entityId%3Dhttps%3A%2F%2Fwww.gradescope.com%2Fauth%2Fsaml%2Fberkeley'
response = requests.get(url)
doc = BeautifulSoup(response.text, 'html.parser')

text = doc.findAll('input')

for t in text:
    print(t)
    print("")

login_url = ("https://auth.berkeley.edu/cas/login")
