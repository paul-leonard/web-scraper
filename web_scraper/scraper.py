'''
Feature Requirements:
- [x] get_citations_needed_count:  takes in a url and returns an integer
- [ ] get_citations_needed_report:  takes in a url and returns a string
- [ ] the string should be formatted with each citation needed on own line, in order found.
'''

import requests
from bs4 import BeautifulSoup
import re


def get_soup_from_site(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  # soup.prettify()
  return soup

def get_citations_needed_count(url):
  soup = get_soup_from_site(url)
  all_citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
  #all_citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
  #for citation_needed in all_citations_needed:
  # each new citation is a new BeautifulSoup object.
  # it has each of the same methods available as the original soup
  #  print(citation_needed, end="\n"*3)
  return len(all_citations_needed)
  
def get_citations_needed_report(url):
  soup = get_soup_from_site(url)

  # all_passages_needing = soup.find_all('p', "citation needed")
  all_passages_needing = soup.find_all('p', text="miles of dirt roads")
  #maybe I need to use regex to say anything can before or after these strings...
  #or try an alternate method of asking what the parent tag is that contains the <sup>...
  # partial_with_regex = re.compile('*miles of dirt roads*')
  # all_passages_needing = soup.find_all('p', text=partial_with_regex)

  print("the number of passages is: ",len(all_passages_needing))
  print("all_passages_needing: *************",all_passages_needing)
  print("************************")

  for passage_needing in all_passages_needing:
    # each new citation is a new BeautifulSoup object.
    # it has each of the same methods available as the original soup
    print(passage_needing.text, end="\n"*3)

  return 



if __name__ == "__main__":
  url = 'https://en.wikipedia.org/wiki/Times_Beach,_Missouri'
  print(get_citations_needed_count(url))
  print(get_citations_needed_report(url))
