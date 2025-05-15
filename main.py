import logging
from scraper.remoteok_scraper import RemoteOKScraper
from storage.data_handler import DataHandler
from analysis.nlp_processor import NLPProcessor
from analysis.visualizer import Visualizer
from config import SCRAPER_CONFIG, DATA_DIR, OUTPUT_DIR
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    try:
        # Step 1: Scrape job data
        scraper = RemoteOKScraper(SCRAPER_CONFIG["REMOTEOK"])
        jobs = scraper.scrape()
        
        # Step 2: Save raw data
        data_handler = DataHandler()
        csv_path = data_handler.save_to_csv(jobs, "remote_jobs.csv")
        
        # Step 3: Analyze data
        df = pd.DataFrame(jobs)
        nlp = NLPProcessor()
        analysis_results = nlp.analyze_jobs(df)
        
        # Step 4: Visualize results
        viz = Visualizer()
        viz.plot_word_frequencies(
            analysis_results['skill_frequencies'],
            "Top Required Skills in Remote Jobs",
            "top_skills.png"
        )
        viz.plot_pie_chart(
            dict(list(analysis_results['location_distribution'].items())[:10]),
            "Job Distribution by Location (Top 10)",
            "location_distribution.png"
        )
        
        logging.info("Job intelligence analysis completed successfully!")
        
    except Exception as e:
        logging.error(f"Application failed: {e}", exc_info=True)

if __name__ == "__main__":
    main()