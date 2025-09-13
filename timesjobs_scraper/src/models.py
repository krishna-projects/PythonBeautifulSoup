from dataclasses import dataclass
from typing import Optional

@dataclass
class JobListing:
    """Represents a job listing with all its attributes."""
    title: str
    company: str
    posted_date: str
    location: str
    experience: str
    job_link: str
    
    @classmethod
    def from_dict(cls, data: dict) -> 'JobListing':
        """Create a JobListing instance from a dictionary."""
        return cls(
            title=data.get('title', ''),
            company=data.get('company', ''),
            posted_date=data.get('posted_date', 'N/A'),
            location=data.get('location', 'N/A'),
            experience=data.get('experience', 'N/A'),
            job_link=data.get('job_link', '')
        )
    
    def to_dict(self) -> dict:
        """Convert the JobListing to a dictionary."""
        return {
            'title': self.title,
            'company': self.company,
            'posted_date': self.posted_date,
            'location': self.location,
            'experience': self.experience,
            'job_link': self.job_link
        }
