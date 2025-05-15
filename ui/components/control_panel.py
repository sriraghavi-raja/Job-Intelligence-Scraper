from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, 
                            QLabel, QLineEdit, QPushButton, QComboBox)
from PyQt5.QtCore import pyqtSignal

class ControlPanel(QWidget):
    start_scraping = pyqtSignal(dict)  # Emits scraping parameters
    
    def __init__(self):
        super().__init__()
        self._init_ui()
        
    def _init_ui(self):
        layout = QVBoxLayout()
        
        # Source Selection
        source_group = QGroupBox("Data Source")
        source_layout = QHBoxLayout()
        
        self.source_combo = QComboBox()
        self.source_combo.addItems(["RemoteOK", "Indeed", "LinkedIn (Demo)"])
        
        source_layout.addWidget(QLabel("Select Source:"))
        source_layout.addWidget(self.source_combo)
        source_group.setLayout(source_layout)
        
        # Parameters
        param_group = QGroupBox("Scraping Parameters")
        param_layout = QVBoxLayout()
        
        self.keyword_input = QLineEdit()
        self.keyword_input.setPlaceholderText("Enter keywords (comma separated)")
        
        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText("Location filter (optional)")
        
        self.max_pages_input = QLineEdit("3")
        
        param_layout.addWidget(QLabel("Keywords:"))
        param_layout.addWidget(self.keyword_input)
        param_layout.addWidget(QLabel("Location:"))
        param_layout.addWidget(self.location_input)
        param_layout.addWidget(QLabel("Max Pages:"))
        param_layout.addWidget(self.max_pages_input)
        param_group.setLayout(param_layout)
        
        # Action Buttons
        button_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start Scraping")
        self.export_btn = QPushButton("Export Data")
        self.settings_btn = QPushButton("Settings")
        
        button_layout.addWidget(self.start_btn)
        button_layout.addWidget(self.export_btn)
        button_layout.addWidget(self.settings_btn)
        
        # Connect signals
        self.start_btn.clicked.connect(self._on_start)
        
        # Assemble main layout
        layout.addWidget(source_group)
        layout.addWidget(param_group)
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def _on_start(self):
        params = {
            "source": self.source_combo.currentText(),
            "keywords": self.keyword_input.text().split(','),
            "location": self.location_input.text(),
            "max_pages": int(self.max_pages_input.text())
        }
        self.start_scraping.emit(params)