import csv
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Union, TypeVar, Generic

from .models import JobListing

T = TypeVar('T')
JobList = List[Union[Dict, JobListing]]

def save_to_csv(jobs: JobList, filename: str) -> None:
    """Save job listings to a CSV file."""
    if not jobs:
        return
    
    # Ensure directory exists
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert JobListing objects to dictionaries if needed
    jobs_data = [job.to_dict() if hasattr(job, 'to_dict') else job for job in jobs]
    
    # Write to CSV
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=jobs_data[0].keys())
        writer.writeheader()
        writer.writerows(jobs_data)

def save_to_json(jobs: JobList, filename: str) -> None:
    """Save job listings to a JSON file."""
    if not jobs:
        return
    
    # Ensure directory exists
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert JobListing objects to dictionaries if needed
    jobs_data = [job.to_dict() if hasattr(job, 'to_dict') else job for job in jobs]
    
    # Write to JSON
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(jobs_data, f, indent=2, ensure_ascii=False)

def generate_filename(base_name: str, extension: str = 'csv') -> str:
    """Generate a timestamped filename."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"data/processed/{base_name}_{timestamp}.{extension}"
