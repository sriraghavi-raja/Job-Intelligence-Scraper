from PyQt5.QtWidgets import (QMainWindow, QTabWidget, QStatusBar, 
                            QWidget, QVBoxLayout)
from PyQt5.QtCore import Qt
from ui.components.control_panel import ControlPanel
from ui.components.job_table import JobTable
from ui.components.chart_widget import ChartWidget
from ui.components.status_bar import CustomStatusBar
from ui.styles import stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Job Intelligence Scraper")
        self.setMinimumSize(1024, 768)
        self.setStyleSheet(stylesheet)
        
        # Central Widget with Tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Setup UI Components
        self._setup_control_panel()
        self._setup_job_table()
        self._setup_charts()
        self._setup_status_bar()
        
    def _setup_control_panel(self):
        """Control panel with scraping parameters"""
        self.control_panel = ControlPanel()
        control_tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.control_panel)
        control_tab.setLayout(layout)
        self.tabs.addTab(control_tab, "Controls")

    def _setup_job_table(self):
        """Table showing scraped jobs"""
        self.job_table = JobTable()
        self.tabs.addTab(self.job_table, "Job Listings")

    def _setup_charts(self):
        """Tab for visualizations"""
        self.chart_widget = ChartWidget()
        chart_tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.chart_widget)
        chart_tab.setLayout(layout)
        self.tabs.addTab(chart_tab, "Analytics")

    def _setup_status_bar(self):
        """Custom status bar with progress indicators"""
        self.status_bar = CustomStatusBar()
        self.setStatusBar(self.status_bar)