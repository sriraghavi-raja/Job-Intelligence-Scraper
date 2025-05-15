from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()
        
    def _init_ui(self):
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        
        # Skills Tab
        self.skills_tab = QWidget()
        self.skills_figure = Figure()
        self.skills_canvas = FigureCanvas(self.skills_figure)
        skills_layout = QVBoxLayout()
        skills_layout.addWidget(self.skills_canvas)
        self.skills_tab.setLayout(skills_layout)
        
        # Locations Tab
        self.locations_tab = QWidget()
        self.locations_figure = Figure()
        self.locations_canvas = FigureCanvas(self.locations_figure)
        locations_layout = QVBoxLayout()
        locations_layout.addWidget(self.locations_canvas)
        self.locations_tab.setLayout(locations_layout)
        
        self.tabs.addTab(self.skills_tab, "Skills Analysis")
        self.tabs.addTab(self.locations_tab, "Location Distribution")
        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    
    def plot_skills(self, skill_data):
        """Plot skills frequency chart"""
        self.skills_figure.clear()
        ax = self.skills_figure.add_subplot(111)
        
        sns.barplot(
            x=list(skill_data.values()),
            y=list(skill_data.keys()),
            ax=ax,
            palette="viridis"
        )
        ax.set_title("Top Required Skills")
        self.skills_canvas.draw()
    
    def plot_locations(self, location_data):
        """Plot location distribution chart"""
        self.locations_figure.clear()
        ax = self.locations_figure.add_subplot(111)
        
        top_locations = dict(list(location_data.items())[:10])
        ax.pie(
            top_locations.values(),
            labels=top_locations.keys(),
            autopct='%1.1f%%'
        )
        ax.set_title("Job Distribution by Location")
        self.locations_canvas.draw()