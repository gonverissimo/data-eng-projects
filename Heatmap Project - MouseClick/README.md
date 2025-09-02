# Mouse Click Heatmap Project

This **Data Engineering** project captures and visualizes user click behavior on a website using **Python**. It simulates how a data engineer might collect, process, and analyze interaction data to generate actionable insights on user behavior.

The primary goal of this project is to **practice data engineering workflows** by tracking user events, processing them, and producing visualizations that show areas of high and low engagement on a web page.

This hands-on project allowed me to:
- Practice **data collection and simulation** of user clicks;
- Process click event data using **Pandas**;
- Generate **heatmaps** with **Matplotlib** and **Seaborn** for visual analytics.

---

## Project Structure

The project contains:

- `generate_clicks.py` – generates simulated click data and exports it to a CSV file (`clicks.csv`).  
- `clicks.csv` – example dataset of simulated user clicks with X/Y coordinates and timestamps.  
- `heatmap.py` – reads the CSV and generates heatmaps (`.png`) visualizing click frequency. Supports optional overlay of a webpage screenshot.  
- `.venv/` – Python virtual environment containing project dependencies.  
- `requirements.txt` – lists all Python packages required for the project (`pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `Pillow`).  

---

## Commands Used

- Set up Python environment:
python -m venv .venv
.\.venv\Scripts\activate 
pip install -r requirements.txt

- Generate a CSV file (clicks.csv) with simulated user click coordinates:
python generate_clicks.py --n 2000 --width 1366 --height 768 --out clicks.csv

- Create heatmap:
python heatmap.py --csv clicks.csv --width 1366 --height 768 --method hist --bins 300 --sigma 4 --output heatmap_hist.png

At the end of this workflow, a PNG file (heatmap.png) is generated showing the frequency of simulated user clicks across the page.