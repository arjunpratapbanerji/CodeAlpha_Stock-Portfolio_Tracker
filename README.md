# Stock Portfolio Tracker

An interactive command-line application built in Python that helps users track, manage, and calculate the value of their stock investments. This project showcases foundational programming concepts such as dictionaries, user input validation, file handling, and automated unit testing.

---

## 🚀 Features
- **Predefined Stock Catalogue**: Pre-loaded with major stocks (Apple, Tesla, Microsoft, etc.) and manually set prices.
- **Dynamic Portfolio Operations**: Add new stocks or update existing share quantities dynamically.
- **Safety Validations**: Prevents application crashes from wrong characters, empty fields, or negative number entries.
- **Value Calculator**: Automatically calculates individual stock values and computes a grand total value for the entire portfolio.
- **Exporting Options**: Save and export formatted reports as human-readable Text files (`.txt`) or spreadsheet-friendly Comma-Separated Values files (`.csv`).
- **Automated Testing Suite**: Includes unit tests verifying calculation correctness and dictionary mappings.

---

## 📂 File Structure
- `main.py`: The core application program logic and command-line user interface.
- `test.py`: The unit test suite using Python's built-in `unittest` library.
- `.gitignore`: Configured to keep the repository clean from cache files and locally exported reports.

---

## ⚙️ Installation & Run Guide

### Prerequisites
- **Python 3.x** installed on your system.

### How to Run the App
1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd C:\Users\ASUS\Desktop\StockTracker
   ```
3. Launch the application:
   ```bash
   python main.py
   # Or using the Windows Python launcher:
   py main.py
   ```

### How to Run Unit Tests
To verify calculations and program logic:
```bash
python test.py
# Or:
py test.py
```
