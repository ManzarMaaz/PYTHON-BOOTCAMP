# 🎓 College Major Salary Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

## 📊 Overview
This project is a data exploration analysis using **Python** and **Pandas** to investigate the relationship between college majors and post-graduation salaries. 

Using a dataset of salaries by college major, this script answers critical questions about financial return on investment (ROI) for various degrees, analyzing starting salaries, mid-career growth, and salary stability.

## ❓ Key Questions Answered
The analysis dives into the data to find:
* **Highest Earners:** Which degrees offer the highest starting and mid-career salaries?
* **Lowest Earners:** Which majors have the lowest earning potential?
* **Risk vs. Reward:** Calculating the "Spread" (difference between 10th and 90th percentile earners) to identify "Low Risk" vs. "High Potential" degrees.
* **Category Analysis:** How do STEM, Business, and HASS (Humanities, Arts, Social Science) degrees compare on average?

## 🛠️ Tech Stack
* **Python:** Core programming language.
* **Pandas:** Used for DataFrames, data cleaning, sorting, grouping, and aggregation.

## 🚀 How to Run
1.  Clone the repository.
2.  Ensure you have `pandas` installed:
    ```bash
    pip install pandas
    ```
3.  Place the `salaries_by_college_major.csv` file in the correct directory.
4.  Run the notebook or script to see the analysis outputs.

## 📈 Methodology
1.  **Data Cleaning:** Handled missing values (`NaN`) to ensure accurate statistical calculations.
2.  **Statistical Analysis:** Used `.max()`, `.min()`, and `.idxmax()` to identify outliers and leaders.
3.  **Feature Engineering:** Created a `'Spread'` column to quantify the salary gap between the top and bottom earners in each major.
4.  **Grouping:** Aggregated data by `'Group'` (e.g., STEM, Business) to derive category-level insights.

---
*This project was completed as part of the #100DaysOfCode challenge.*
