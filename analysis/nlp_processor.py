import re
import pandas as pd
import nltk
from collections import Counter
from typing import List, Dict, Tuple
from config import NLP_CONFIG
import logging
import os

class NLPProcessor:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self._ensure_nltk_resources()
        self.stopwords = set()
        for lang in NLP_CONFIG["STOPWORDS_LANGUAGES"]:
            self.stopwords.update(nltk.corpus.stopwords.words(lang))
        self.skills_db = NLP_CONFIG["SKILLS_DB"]
        self.min_word_length = NLP_CONFIG["MIN_WORD_LENGTH"]
        self._verify_punkt_installation()

    def _ensure_nltk_resources(self):
        resources = [
            ('punkt', 'tokenizers/punkt'),
            ('stopwords', 'corpora/stopwords'),
            ('wordnet', 'corpora/wordnet'),
            ('averaged_perceptron_tagger', 'taggers/averaged_perceptron_tagger')
        ]
        
        for resource_name, resource_path in resources:
            try:
                nltk.data.find(resource_path)
                self.logger.info(f"NLTK resource found: {resource_name}")
            except LookupError:
                self.logger.warning(f"Downloading NLTK resource: {resource_name}")
                try:
                    nltk.download(resource_name)
                except Exception as e:
                    self.logger.error(f"Failed to download {resource_name}: {e}")
                    raise

    def _verify_punkt_installation(self):
        try:
            # Test the punkt tokenizer
            nltk.word_tokenize("This is a test.")
        except LookupError as e:
            self.logger.error("Punkt tokenizer verification failed!")
            self.logger.error("Trying alternative installation method...")
            self._alternative_punkt_install()
            
    def _alternative_punkt_install(self):
        """Alternative method for punkt installation"""
        try:
            import urllib.request
            import zipfile
            import shutil
            import tempfile
            
            punkt_url = "https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip"
            target_dir = os.path.join(nltk.data.path[0], 'tokenizers', 'punkt')
            
            self.logger.info(f"Downloading punkt directly to {target_dir}")
            
            # Create temp directory
            temp_dir = tempfile.mkdtemp()
            zip_path = os.path.join(temp_dir, 'punkt.zip')
            
            # Download zip
            urllib.request.urlretrieve(punkt_url, zip_path)
            
            # Extract zip
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(target_dir)
                
            self.logger.info("Punkt installed successfully via alternative method")
        except Exception as e:
            self.logger.error(f"Alternative installation failed: {e}")
            raise

    def preprocess_text(self, text: str) -> List[str]:
        try:
            # Simple fallback tokenizer if punkt fails
            if not text:
                return []
                
            text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
            
            try:
                tokens = nltk.word_tokenize(text)
            except:
                # Fallback to simple whitespace tokenizer
                tokens = text.split()
                
            return [
                token for token in tokens 
                if token not in self.stopwords 
                and len(token) >= self.min_word_length
                and token.isalpha()
            ]
        except Exception as e:
            self.logger.error(f"Error in text preprocessing: {e}")
            return []

    def extract_skills(self, text: str) -> List[str]:
        tokens = self.preprocess_text(text)
        text_lower = ' '.join(tokens).lower()
        return [skill for skill in self.skills_db if skill in text_lower]

    def analyze_jobs(self, df: pd.DataFrame) -> Dict:
        try:
            # Combine all relevant text fields
            text_data = (
                df['title'].str.cat(sep=' ') + ' ' +
                df['tags'].apply(lambda x: ' '.join(x) if isinstance(x, list) else '').str.cat(sep=' ')
            )
            
            # Get word frequencies
            tokens = self.preprocess_text(text_data)
            word_freq = Counter(tokens) if tokens else {}
            
            # Get skill frequencies
            skills = self.extract_skills(text_data)
            skill_freq = Counter(skills)
            
            # Location analysis
            location_dist = df['location'].value_counts().to_dict()
            
            return {
                'word_frequencies': word_freq,
                'skill_frequencies': skill_freq,
                'location_distribution': location_dist,
                'top_companies': df['company'].value_counts().head(10).to_dict()
            }
        except Exception as e:
            self.logger.error(f"Error in job analysis: {e}")
            return {
                'word_frequencies': {},
                'skill_frequencies': {},
                'location_distribution': {},
                'top_companies': {}
            }