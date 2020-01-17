import requests
from bs4 import BeautifulSoup as soup

def extract_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    source=requests.get(url, headers=headers).text
    return source

data=extract_source('https://www.narendramodi.in/category/text-speeches')
parsed_data=soup(data)

speech_link=parsed_data.findAll('a',{'class':'left_class'})

links=[link['href'] for link in speech_link]

links.append('https://www.narendramodi.in/pm-modi-s-text-of-speech-in-delhi-s-ramlila-maidan-547768')
links.append('https://www.narendramodi.in/pm-modi-s-text-of-speech-at-barhait-in-jharkhand-547690')
links.append('https://www.narendramodi.in/pm-modi-s-text-of-speech-at-dumka-in-jharkhand-s--547689')
links.append('https://www.narendramodi.in/text-of-pm-modi-s-speech-at-public-meeting-in-dhanbad-jharkhand-547632')
links.append('https://www.narendramodi.in/text-of-pm-s-speech-at-public-meeting-in-barhi-jharkhand-547615')
links.append('https://www.narendramodi.in/text-of-pm-s-address-at-the-hindustan-times-leadership-summit-547561')
links.append('https://www.narendramodi.in/text-of-pm-modi-s-speech-at-public-meeting-in-khunti-jharkhand-547536')
links.append('https://www.narendramodi.in/text-of-pm-s-address-at-republic-tv-summit-547464')
links.append('https://www.narendramodi.in/text-of-pm-s-speech-at-conclave-of-accountants-general-deputy-accountants-general-547384')
links.append('https://www.narendramodi.in/text-of-pm-s-remarks-on-250th-session-of-rajya-sabha-547353')
links.append('https://www.narendramodi.in/text-of-pm-s-statement-to-media-ahead-of-winter-session-of-parliament-547348')


final_links=[]

for link in links:
    if link not in final_links:
        final_links.append(link)

print(final_links)

corpus_text=[]

for link in final_links:
    ind_data=extract_source(link)
    parsed_data=soup(ind_data)
    #print(parsed_data)
    hindi_text=parsed_data.findAll('p',{'style':'text-align: justify;'})
    final_text=''''''
    for tags in hindi_text:
        final_text=final_text+tags.text

    corpus_text.append(final_text)

with open('data.txt', 'w',encoding="utf-8") as f:
    for item in corpus_text:
        f.write("%s\n" % item)

    

