from PyQt5.QtWidgets import QStatusBar, QLabel, QProgressBar
from PyQt5.QtCore import Qt

class CustomStatusBar(QStatusBar):
    def __init__(self):
        super().__init__()
        self._init_ui()
        
    def _init_ui(self):
        self.status_label = QLabel("Ready")
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumWidth(200)
        self.progress_bar.setVisible(False)
        
        self.addWidget(self.status_label, 1)
        self.addPermanentWidget(self.progress_bar)
    
    def set_progress(self, value, maximum=100):
        self.progress_bar.setMaximum(maximum)
        self.progress_bar.setValue(value)
        self.progress_bar.setVisible(True)
    
    def reset_progress(self):
        self.progress_bar.reset()
        self.progress_bar.setVisible(False)
    
    def set_message(self, text):
        self.status_label.setText(text)