'''
Feature Requirements:
- [x] get_citations_needed_count:  takes in a url and returns an integer
- [ ] get_citations_needed_report:  takes in a url and returns a string
- [ ] the string should be formatted with each citation needed on own line, in order found.
'''

import requests
from bs4 import BeautifulSoup


def get_soup_from_site(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  # soup.prettify()
  return soup

def get_citations_needed_count(url):
  soup = get_soup_from_site(url)
  all_citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
  return len(all_citations)
  
def get_citations_needed_report(url):
  soup = get_soup_from_site(url)
  all_citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
  for citation in all_citations:
  # each new citation is a new BeautifulSoup object.
  # it has each of the same methods available as the original soup
    print(citation, end="\n"*3)

  pass






if __name__ == "__main__":
  url = 'https://en.wikipedia.org/wiki/Times_Beach,_Missouri'
  print(get_soup_from_site(url))
  print(get_citations_needed_count(url))