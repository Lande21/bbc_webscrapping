import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = 'https://www.bbc.com/news'

# Fetch the webpage content
response = requests.get(url)
if response.status_code == 200:
    webpage_content = response.text
else:
    print(f"Failed to retrieve webpage. Status code: {response.status_code}")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(webpage_content, 'html.parser')

# Debugging: Print the HTML of the first 1000 characters to check the structure
print(soup.prettify()[:1000])

# Extract the headlines
headlines = soup.find_all('h3', class_='gs-c-promo-heading')

if not headlines:
    print("No headlines found. The structure of the website may have changed.")

for idx, headline in enumerate(headlines, start=1):
    print(f"{idx}. {headline.text.strip()}")
