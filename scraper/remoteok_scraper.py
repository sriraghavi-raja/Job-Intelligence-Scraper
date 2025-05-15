from .base_scraper import BaseScraper
from bs4 import BeautifulSoup
from typing import List, Dict
import pandas as pd
from datetime import datetime

class RemoteOKScraper(BaseScraper):
    def scrape(self, max_pages: int = None) -> List[Dict]:
        max_pages = max_pages or self.config.get("MAX_PAGES", 1)
        base_url = self.config["BASE_URL"]
        all_jobs = []
        
        for page in range(1, max_pages + 1):
            url = f"{base_url}?page={page}" if page > 1 else base_url
            soup = self.fetch_page(url)
            if not soup:
                continue
                
            jobs = self._parse_page(soup)
            all_jobs.extend(jobs)
            
        return all_jobs

    def _parse_page(self, soup: BeautifulSoup) -> List[Dict]:
        jobs = []
        job_rows = soup.find_all("tr", class_="job")
        
        for row in job_rows:
            try:
                job = {
                    "title": self._clean_text(row.find("h2")),
                    "company": self._clean_text(row.find("h3")),
                    "location": self._clean_text(row.find("div", class_="location"), default="Remote"),
                    "salary": self._clean_text(row.find("div", class_="salary")),
                    "tags": [tag.text.strip() for tag in row.find_all("div", class_="tag")],
                    "posted": self._clean_text(row.find("time")),
                    "url": self._make_absolute_url(self.config["BASE_URL"], row.get("data-href", "")),
                    "scraped_at": datetime.now().isoformat()
                }
                jobs.append(job)
            except Exception as e:
                self.logger.error(f"Error parsing job row: {e}")
                
        return jobs

    def _clean_text(self, element, default=""):
        return element.text.strip() if element else default