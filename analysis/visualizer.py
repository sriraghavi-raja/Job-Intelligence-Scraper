import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict
from pathlib import Path
from config import OUTPUT_DIR
import logging

class Visualizer:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        sns.set_theme(style="whitegrid")
        plt.style.use('ggplot')

    def plot_word_frequencies(self, frequencies: Dict[str, int], title: str, filename: str, top_n: int = 15):
        try:
            top_words = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:top_n])
            
            plt.figure(figsize=(12, 8))
            ax = sns.barplot(x=list(top_words.values()), y=list(top_words.keys()), palette="viridis")
            ax.set_title(title, fontsize=16)
            ax.set_xlabel("Frequency", fontsize=12)
            ax.set_ylabel("Term", fontsize=12)
            
            self._save_plot(filename)
        except Exception as e:
            self.logger.error(f"Error plotting word frequencies: {e}")
            raise

    def plot_pie_chart(self, data: Dict[str, int], title: str, filename: str):
        try:
            plt.figure(figsize=(10, 10))
            plt.pie(
                x=list(data.values()),
                labels=list(data.keys()),
                autopct='%1.1f%%',
                startangle=90,
                pctdistance=0.85,
                labeldistance=1.05
            )
            plt.title(title, fontsize=16)
            plt.tight_layout()
            
            self._save_plot(filename)
        except Exception as e:
            self.logger.error(f"Error plotting pie chart: {e}")
            raise

    def _save_plot(self, filename: str):
        filepath = OUTPUT_DIR / filename
        plt.savefig(filepath, bbox_inches='tight', dpi=300)
        plt.close()
        self.logger.info(f"Plot saved to {filepath}")