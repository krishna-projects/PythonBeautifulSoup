import csv
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict

def save_to_csv(jobs: List[Dict], filename: str) -> None:
    """Save job listings to a CSV file."""
    if not jobs:
        return
    
    # Ensure directory exists
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Write to CSV
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=jobs[0].keys())
        writer.writeheader()
        writer.writerows(jobs)

def save_to_json(jobs: List[Dict], filename: str) -> None:
    """Save job listings to a JSON file."""
    if not jobs:
        return
    
    # Ensure directory exists
    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Write to JSON
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)

def generate_filename(base_name: str, extension: str = 'csv') -> str:
    """Generate a timestamped filename."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"data/processed/{base_name}_{timestamp}.{extension}"
