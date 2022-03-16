import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=object+detection+in+aerial+image+&btnG=&oq=ob'

response = requests.get(url, headers=headers)

response.status_code

page_contents = response.text

len(page_contents)

doc = BeautifulSoup(page_contents,'html.parser')
type(doc)


#Paper name

paper_name_tag = doc.select('[data-lid]')

paper_names = []
for tag in paper_name_tag:
    paper_names.append(tag.select('h3')[0].get_text())

paper_names



#link of the paper
links = paper_name_tag[0].find('h3')
link_tag = doc.find_all('h3',{"class" : "gs_rt"})
link_tag[0]

link_tag[0].a['href']

links = []

for i in range(len(link_tag)) :
  links.append(link_tag[i].a['href'])

print(links)

#Authors of the paper
authors_tag = doc.find_all("div", {"class": "gs_a"})
len(authors_tag)

authors_tag[0]

authors_tag[4].text
x = authors_tag[0].find('a').text

authors_list = []
for i in authors_tag:
  authors_list.append(i.text)

print(authors_list)


#Create CSV file(s) with extracted information
import pandas as pd
paper_dict = {
    'paper title ' : paper_names,
    'authors' : authors_list,
    'url of paper' : links
}

papers_df = pd.DataFrame(paper_dict)

print(papers_df)
