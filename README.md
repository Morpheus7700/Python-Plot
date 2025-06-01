Python Plot: PR vs GHI Analysis with Visualization
This repository contains a Python-based data processing and visualization project that merges and analyzes solar plant performance data (PR) and solar irradiance data (GHI).

🔧 What This Project Does:
Combines daily performance ratio (PR) and global horizontal irradiance (GHI) data from multiple CSV files.

Generates a merged dataset with a standardized format for further analysis.

Visualizes PR trends over time using a combination of:

Color-coded scatter plots based on GHI levels.

A 30-day moving average trendline.

A dynamic budget line that decreases annually by 0.8%.

Display of recent average PR values (7, 30, and 60 days) for performance tracking.

📁 Files Included:
merged_data.csv – The processed and cleaned dataset.

PV Doctor Project CSV Compile.py – Python script for merging PR and GHI data files.

PV Doctor Graph.py – Script for generating the final visualization with matplotlib.

your_graph.jpg – Output graph showing PR trends with budget and average overlays.

📈 Visualization Features:
Color-coded PR scatter points based on GHI thresholds.

30-day moving average to visualize performance trends.

Year-wise decreasing budget line for target comparison.

Dynamic annotations for latest PR averages.

✅ Requirements:
Python 3.x

Libraries: pandas, matplotlib
