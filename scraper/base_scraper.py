import requests
from bs4 import BeautifulSoup
import time
import random
from typing import Dict, List, Optional
from urllib.parse import urljoin
import logging

class BaseScraper:
    def __init__(self, config: Dict):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update(config.get("HEADERS", {}))
        self.logger = logging.getLogger(self.__class__.__name__)

    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        try:
            response = self.session.get(url)
            response.raise_for_status()
            self._random_delay()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            self.logger.error(f"Error fetching {url}: {e}")
            return None

    def _random_delay(self):
        delay = self.config.get("DELAY", 1) * random.uniform(0.9, 1.1)
        time.sleep(delay)

    def scrape(self, *args, **kwargs) -> List[Dict]:
        raise NotImplementedError("Subclasses must implement this method")

    def _make_absolute_url(self, base_url: str, path: str) -> str:
        return urljoin(base_url, path)