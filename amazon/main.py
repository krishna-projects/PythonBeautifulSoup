from bs4 import BeautifulSoup   
import requests
import os
import re
import time

def get_cached_html(url):
    # Get the directory where the current script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Script directory {script_dir}")
    
    # Create the full path to the subdirectory
    filename = re.search(r'/dp/([A-Z0-9]{10})', url).group(1)
    file = os.path.join(script_dir, f"data/{filename}.html")
    print(f"file path {file}")
    
    if os.path.exists(file):
        print("file already present, getting from local")
        with open(file,"r") as file:
            return file.read()
    else:
        print("getting html file from internet")
        html = requests.get(url)
        with open(file, "w") as file:
            print(html)
            file.write(html.text)
            return html
    

def get_html(url):
    html = requests.get(url)
    return html.text

"""
# Find first matching element
soup.find('tag_name')              # Find by tag
soup.find(id='element_id')         # Find by ID
soup.find(class_='class_name')     # Find by class (note the underscore)
soup.find(attrs={'data-attr': 'value'})  # Find by attribute

# Using CSS selectors
soup.select_one('css_selector')    # Returns first match

# Find all matching elements
soup.find_all('tag_name')          # Find all by tag
soup.find_all(class_='class_name') # Find all by class
soup.find_all('tag', class_='class_name')  # Multiple conditions
soup.select('css_selector')        # Find all using CSS selector

# Navigation
element.parent                     # Parent element
element.contents                   # Direct children as a list
element.children                   # Iterate over children
element.descendants                # All descendants (recursive)
element.next_sibling               # Next element at same level
element.previous_sibling           # Previous element at same level
element.find_next_sibling()        # Next sibling matching criteria
element.find_previous_sibling()    # Previous sibling matching criteria

# Text and attributes
element.text                       # Get text content (all child text nodes)
element.get_text(separator=' ')    # Get text with custom separator
element.string                     # Get text if only one child is a string
element['attribute_name']          # Get attribute value
element.get('attribute_name')      # Safer way to get attribute 
element.get('attribute_name', 'default_value')  # With default value
element.attrs                      # Get all attributes as dict 
"""

def scrapeAmazon(soup):
    print(f"page title : {soup.find("title").text}")
    print(f"product title {soup.select("#productTitle")[0].text.strip()}") 
    print(f"price of product : {soup.find(class_='a-price-whole').text}") 
    # getting list of images
    imageElements = soup.select("div#altImages > ul > li.item:not(.videoBlockIngress)")
    print(f"size of image list = {len(imageElements)}")

    for image in imageElements:
        imageThumbLink = image.find("img").get('src')
        imageUrl = imageThumbLink.replace("._SS40_","")
        print(f"{imageUrl} \n")
        

    # product details
    productDetails = soup.select("li.a-spacing-mini > span.a-list-item")
    for detail in productDetails:
        print(detail.text.strip())


start = time.time()
url = "https://www.amazon.in/Marshall-Emberton-Wireless-Bluetooth-Portable/dp/B09XXW54QG"
html = get_cached_html(url)
soup = BeautifulSoup(html,"lxml")

if "amazon" in url:
    scrapeAmazon(soup)
else:
    print("url is not from amazon")

print(f"finished in {time.time() - start} seconds")