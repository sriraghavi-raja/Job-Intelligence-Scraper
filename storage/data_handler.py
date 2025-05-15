import pandas as pd
import json
from pathlib import Path
from typing import List, Dict
import logging
from config import DATA_DIR

class DataHandler:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def save_to_csv(self, data: List[Dict], filename: str) -> Path:
        filepath = DATA_DIR / filename
        try:
            df = pd.DataFrame(data)
            df.to_csv(filepath, index=False)
            self.logger.info(f"Data saved to {filepath}")
            return filepath
        except Exception as e:
            self.logger.error(f"Error saving to CSV: {e}")
            raise

    def save_to_json(self, data: List[Dict], filename: str) -> Path:
        filepath = DATA_DIR / filename
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            self.logger.info(f"Data saved to {filepath}")
            return filepath
        except Exception as e:
            self.logger.error(f"Error saving to JSON: {e}")
            raise

    def load_data(self, filename: str) -> pd.DataFrame:
        filepath = DATA_DIR / filename
        try:
            if filepath.suffix == '.csv':
                return pd.read_csv(filepath)
            elif filepath.suffix == '.json':
                with open(filepath, 'r', encoding='utf-8') as f:
                    return pd.DataFrame(json.load(f))
            else:
                raise ValueError("Unsupported file format")
        except Exception as e:
            self.logger.error(f"Error loading data: {e}")
            raise