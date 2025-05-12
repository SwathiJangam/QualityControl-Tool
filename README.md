# Visual Quality Control (VQC) Tool

A Python-based GUI tool for environmental data visualization and cleaning.

## 📊 Features

- Visualize time-series data from `.csv` or `.xlsx`
- Detect spikes and anomalies
- Interactive world map for geospatial visualization (using Basemap)
- Manual flagging of data using:
  - 🟥 Red: Worst data
  - 🟦 Blue: Stuck values
  - 🟨 Yellow: Probably good
  - 🟩 Green: Good data

## 🛠 Tech Stack

- Python
- Tkinter
- Matplotlib
- Pandas
- NumPy
- Basemap

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🚀 Run

```bash
python vqc.py
```

## 📁 Data Files
- 📄 `maindata.csv`
- 📊 `incoisdata.xlsx`

## 📄 Documentation
Refer to *Batch 18 Final Doc.pdf* and *Batch 18 (1).ppt* for design and methodology.

