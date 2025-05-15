import os
os.environ['QT_LOGGING_RULES'] = 'qt.qpa.fonts=false'  # Suppress font warnings
import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from scraper.remoteok_scraper import RemoteOKScraper
from storage.data_handler import DataHandler
from analysis.nlp_processor import NLPProcessor
from analysis.visualizer import Visualizer
from config import SCRAPER_CONFIG
import logging

class JobIntelligenceApp(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.main_window = MainWindow()
        self.main_window.show()
        
        # Initialize components
        self.scraper = RemoteOKScraper(SCRAPER_CONFIG["REMOTEOK"])
        self.data_handler = DataHandler()
        self.nlp_processor = NLPProcessor()
        self.visualizer = Visualizer()
        
        # Connect signals
        self._connect_signals()
        
    def _connect_signals(self):
        """Connect UI signals to slots"""
        self.main_window.control_panel.start_scraping.connect(self.start_scraping)
        
    def start_scraping(self, params):
        """Handle scraping process"""
        try:
            self.main_window.status_bar.set_message("Scraping started...")
            self.main_window.status_bar.set_progress(0, 100)
            
            # Run scraping
            jobs = self.scraper.scrape(max_pages=params['max_pages'])
            
            # Save and analyze
            csv_path = self.data_handler.save_to_csv(jobs, "jobs.csv")
            df = self.data_handler.load_data("jobs.csv")
            analysis = self.nlp_processor.analyze_jobs(df)
            
            # Update UI
            self.main_window.job_table.update_data(df)
            self.main_window.chart_widget.plot_skills(analysis['skill_frequencies'])
            self.main_window.chart_widget.plot_locations(analysis['location_distribution'])
            
            self.main_window.status_bar.set_message("Scraping completed successfully!")
            
        except Exception as e:
            logging.error(f"Scraping failed: {e}")
            self.main_window.status_bar.set_message(f"Error: {str(e)}")
        finally:
            self.main_window.status_bar.reset_progress()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = JobIntelligenceApp(sys.argv)
    sys.exit(app.exec_())