import urllib
import chardet
import requests

#Getting the data from the webpage
data=urllib.request.urlopen('https://google.com').read()

print(chardet.detect(data))

#Output   {'encoding': 'ISO-8859-1', 'confidence': 0.73, 'language': ''}

#For files


f=open('william.txt')
filedata=f.read().encode()#converting string to bytes
print(chardet.detect(filedata))

#Output  {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}

