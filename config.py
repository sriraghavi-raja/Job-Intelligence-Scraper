import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Scraper settings
SCRAPER_CONFIG = {
    "REMOTEOK": {
        "BASE_URL": "https://remoteok.com/remote-dev-jobs",
        "HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        },
        "MAX_PAGES": 3,
        "DELAY": 1.5  # seconds between requests
    }
}

# NLP settings
NLP_CONFIG = {
    "SKILLS_DB": [
        "python", "javascript", "java", "c#", "php", "c++", "ruby", "go",
        "aws", "azure", "gcp", "docker", "kubernetes", "terraform",
        "react", "angular", "vue", "django", "flask", "spring",
        "sql", "mongodb", "postgresql", "mysql", "redis",
        "machine learning", "ai", "nlp", "computer vision",
        "git", "jenkins", "ci/cd", "agile", "scrum"
    ],
    "STOPWORDS_LANGUAGES": ["english"],
    "MIN_WORD_LENGTH": 3
}