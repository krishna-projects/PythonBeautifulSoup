from bs4 import BeautifulSoup   
import requests

def getHtml(url):
    html_text = requests.get(url)
    return BeautifulSoup(html_text.text,"lxml")


soup = getHtml("https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation=")

jobs = soup.find_all('div', class_='srp-listing')
# print(f"Found list with find method: {jobs}")

# listing = soup.select("div.srp-listing")
# print(f"Listing with select: {listingSelect}")

for job in jobs:
    # print(f"printing job: {job}")
    print("===================")
    detailLink = job.find("a")["href"]
    jobName = job.find("h3").text
    jobDesc = job.find("h4").text.split("|")
    company = jobDesc[0].strip()
    posted = jobDesc[1].strip()
    comp = job.find("span",class_="srp-comp-name").text
    print(f"detail link: {detailLink}")
    print(f"job name: {jobName}")
    print(f"comapany: {company}")
    print(f"posted Date: {posted}")
    print(f"company class: {comp}")
    print("===================")