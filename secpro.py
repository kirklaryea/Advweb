import re
import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
best_books= requests.get("https://www.penguinrandomhouse.com/the-read-down/authors-best-books-theyve-received/")

# Parse the HTML content of the page
soup = BeautifulSoup(best_books.content, 'html.parser')

# Finding the paragraph with the desired text
paragraph = soup.find("span", class_="s1")
scraped_para=paragraph.get_text(strip=True)
print('Scraped paragraph:'+'\n'+ scraped_para)

#Using  regular expression to check that a string matched a certain pattern.
pattern = r'\w*\w+e+\b'  # Match words ending with the letter e
pattern_matches = re.findall(pattern, scraped_para)
print("Words end with the letter \"e\":", pattern_matches)
