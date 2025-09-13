import logging
from datetime import datetime
from src.scraper import JobScraper
from src.parser import parse_job_listings
from src.storage import save_to_csv, generate_filename, save_to_json
from config.settings import DEFAULT_PARAMS

def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=f'logs/scraper_{datetime.now().strftime("%Y%m%d")}.log',
        filemode='a'
    )

def main():
    # Set up logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Starting job scraping process")
        
        # Initialize scraper
        scraper = JobScraper()
        # Fetch job listings
        logger.info("Fetching job listings...")
        html_content = scraper.fetch_jobs(DEFAULT_PARAMS)
        
        if not html_content:
            logger.error("Failed to fetch job listings")
            return
            
        # Save raw HTML for debugging
        scraper.save_raw_html(html_content, f"jobs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        
        # Parse job listings
        logger.info("Parsing job listings...")
        jobs = parse_job_listings(html_content)
        
        if not jobs:
            logger.warning("No jobs found in the parsed content")
            return
            
        # Save to CSV
        output_file = generate_filename("jobs", "csv")
        save_to_csv(jobs, output_file)
        save_to_json(jobs,generate_filename("jobs","json"))
        logger.info(f"Successfully saved {len(jobs)} jobs to {output_file}")
        
        # Print summary
        print(f"\nScraping complete!")
        print(f"Total jobs found: {len(jobs)}")
        print(f"Results saved to: {output_file}")
        
    except Exception as e:
        logger.exception("An error occurred during scraping:")
        print(f"An error occurred: {e}")
        
    finally:
        # Clean up
        if 'scraper' in locals():
            scraper.close()
        logger.info("Scraping process completed")

if __name__ == "__main__":
    main()
