import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the website's URL
url = 'https://www.datacentermap.com/'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the list of data centers using the HTML element and class name
data_centers = soup.find_all('div', class_='dcList')

# Extract the data from the HTML tags
for data_center in data_centers:
    name = data_center.find('h2').text
    location = data_center.find('span', class_='dcLoc').text
    print(name, location)
