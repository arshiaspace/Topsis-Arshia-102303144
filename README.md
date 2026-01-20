# Topsis-Arshia-102303144
Implementation of the TOPSIS multi-criteria decision-making method: includes CLI program, Python package, and Flask web service with email functionality.
This repository contains all parts of the TOPSIS assignment:

## Part-I: Command Line TOPSIS Program
- Implemented in Python (`Topsis-Part1/topsis.py`)
- Usage:
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
- Example:
python topsis.py data.csv "1,1,1,2" "+,+,-,+" output-result.csv
- Handles:
- Wrong number of parameters
- File not found
- Non-numeric values
- Weights/Impacts mismatch
- Impacts must be + or -

## Part-II: Python Package (PyPI)
- Package name: `Topsis-Arshia-102303144`
- Package link: https://pypi.org/project/Topsis-Arshia-102303144/1.0.0/
- User manual included in `Topsis-Part2/README.md`
- Install via pip for testing:
  pip install Topsis-Arshia-102303144==1.0.0

## Part-III: TOPSIS Web Service
- Flask-based web application (`Topsis-Part3/app.py`)
- User provides:
- CSV/Excel file
- Weights and impacts (comma-separated)
- Email ID
- Validations:
- Number of weights = number of impacts
- Impacts must be + or -
- Correct email format
- Result is emailed as CSV
- Frontend is modern and responsive
- Instructions:
1. Navigate to `Topsis-Part3/`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python app.py`
4. Open browser: http://127.0.0.1:5000

