from pathlib import Path

def load_stylesheet():
    """Load and return the stylesheet content"""
    stylesheet_path = Path(__file__).parent / "styles.qss"
    with open(stylesheet_path, "r") as f:
        return f.read()

stylesheet = load_stylesheet()