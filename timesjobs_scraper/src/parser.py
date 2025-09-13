from typing import List, Dict
from bs4 import BeautifulSoup, Tag
from config.settings import SELECTORS
from .models import JobListing

def parse_job_listings(html_content: str) -> List[JobListing]:
    """Parse job listings from HTML content and return a list of JobListing objects."""
    soup = BeautifulSoup(html_content, 'lxml')
    job_elements = soup.select(SELECTORS["job_listings"])
    return [parse_job_element(job) for job in job_elements]

def parse_job_element(job: Tag) -> JobListing:
    """Extract job details from a single job element and return a JobListing object."""
    job_title = job.select_one(SELECTORS["job_title"]).text.strip()
    company = job.select_one(SELECTORS["company_name"]).text.strip()
    posted_date = job.select_one(SELECTORS["posted_date"]).text.strip()
    job_link = job.select_one(SELECTORS["job_link"])['href']
    
    # Extract location and experience if available
    exp_loc = job.select_one("div.clearfix.exp-loc")
    location = exp_loc.select_one("div.srp-loc").text.strip() if exp_loc else "N/A"
    experience = exp_loc.select_one("div.srp-exp").text.strip() if exp_loc else "N/A"
    
    return JobListing(
        title=job_title,
        company=company,
        posted_date=posted_date,
        location=location,
        experience=experience,
        job_link=job_link
    )
