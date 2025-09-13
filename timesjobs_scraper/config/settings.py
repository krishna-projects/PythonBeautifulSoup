# Base URL for the job search
BASE_URL = "https://m.timesjobs.com/mobile/jobs-search-result.html"

# Default search parameters
DEFAULT_PARAMS = {
    "txtKeywords": "Python,",
    "cboWorkExp1": "-1",
    "txtLocation": ""
}

# Request headers to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# CSS Selectors
SELECTORS = {
    "job_listings": "div.srp-listing",
    "job_title": "h3 a",
    "company_name": "span.srp-comp-name",
    "posted_date": "span.posting-time",
    "job_link": "a.srp-apply-new"
}
