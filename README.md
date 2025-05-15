
# Job Intelligence Scraper 🚀

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

A powerful web scraping tool that extracts job listings and performs intelligent analysis using NLP, with both CLI and GUI interfaces.

## CLI

![image](https://github.com/user-attachments/assets/004193ed-809e-48c0-9ac2-6b968ba63ffc)

# CSV_FILE

![image](https://github.com/user-attachments/assets/a255314f-a600-4665-8cc8-84163b233b76)



##  GUI
![WhatsApp Image 2025-05-15 at 23 36 21_c01fb44a](https://github.com/user-attachments/assets/f14c814f-2b0d-4ed5-b45e-2df5070c5b86)


![WhatsApp Image 2025-05-15 at 23 36 39_8bb80776](https://github.com/user-attachments/assets/d9bd8b2e-9a18-48ce-9613-791a90f2f07b)

![WhatsApp Image 2025-05-15 at 23 36 51_ddd1f421](https://github.com/user-attachments/assets/041249e1-d2ac-4d1e-8795-f2b6b5463a27)


## Features ✨

- **Multi-source scraping**: RemoteOK, Indeed (demo), LinkedIn (demo)
- **NLP Analysis**: Extract key skills and requirements
- **Data Visualization**: Interactive charts and graphs
- **Modern UI**: PyQt5-based graphical interface
- **Export Options**: CSV, JSON, and image exports
- **Customizable**: Easy to configure and extend

## Installation 💻

### Prerequisites
- Python 3.8+
- pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/job-intelligence-scraper.git
   cd job-intelligence-scraper
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download NLTK data:
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

## Usage 🛠️

### Command Line Interface
```bash
python main.py
```

### Graphical User Interface
```bash
python main_ui.py
```

### Configuration
Edit `config.py` to customize:
- Scraper settings
- NLP parameters
- Output directories

## Project Structure 📂

```
job-intelligence-scraper/
├── scraper/          # Web scraping components
│   ├── base_scraper.py
│   └── remoteok_scraper.py
├── analysis/         # NLP and data analysis
│   ├── nlp_processor.py
│   └── visualizer.py
├── storage/          # Data persistence
│   └── data_handler.py
├── ui/               # Graphical interface
│   ├── components/   # UI widgets
│   ├── styles/       # QSS stylesheets
│   └── main_window.py
├── config.py         # Configuration
├── main.py           # CLI entry point
├── main_ui.py        # GUI entry point
├── requirements.txt  # Dependencies
├── README.md         # Documentation
└── LICENSE           # MIT License
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support 💖

If you find this project useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 💡 Suggesting new features
- 🛠️ Contributing code

---

**Happy job hunting!** 🔍💼
```

### Key Features of This README:

1. **Badges**: Visual indicators for Python version, PyQt5, and license
2. **Modern Formatting**: Emoji icons for better visual scanning
3. **Complete Documentation**: Covers all aspects of the project
4. **Visual Structure**: Clear section headers and code blocks
5. **Responsive Design**: Looks good on GitHub and other Markdown viewers
6. **Call-to-Actions**: Encourages contributions and support

You can copy this directly into your project's `README.md` file. The placeholder image URL can be replaced with an actual screenshot once you have one. Would you like me to add any additional sections or modify any part of this README?
