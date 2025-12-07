# 📈 Stack Overflow Language Trends Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557c?logo=python" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

## 📊 Overview
This project analyzes the historical popularity of programming languages using data from **Stack Overflow**.

By querying the Stack Exchange Data Explorer (SEDE) and processing over 10+ years of post data, this analysis visualizes the rise and fall of languages like Python, Java, and JavaScript. It serves as a study in **Time Series Analysis** and **Data Reshaping** using Python.

---

## 📸 Visualization Preview

| **Raw Time Series** | **Smoothed Trends (Rolling Mean)** |
|:---:|:---:|
| <img width="100%" src="https://github.com/user-attachments/assets/cc7a3c0a-c5a8-4c2f-8a0d-75fe647dff59">  | <img src="https://github.com/user-attachments/assets/2b7b9363-cc2b-4f9e-866e-10c41dca206c" width="100%"> |




---

## ❓ Key Insights
* **The Rise of Python:** Visualized the massive growth of Python post-2012, correlating with the Data Science boom.
* **Java's Stability:** Analyzed Java's consistent high-volume presence over the decade.
* **Niche vs. Mainstream:** Compared volume between mainstream languages (C#, JavaScript) and niche/older ones (Perl, Delphi).
* **Seasonality:** Identified noise in monthly data and smoothed it using a 6-month rolling window to reveal clearer long-term trends.

---

## 🛠️ Tech Stack
* **Python:** Core scripting.
* **Pandas:** Used for `read_csv`, `to_datetime`, `pivot` (reshaping), and `rolling` (smoothing).
* **Matplotlib:** Used for generating line charts with multiple series and custom styling.

## 📂 Project Structure
* `Analysis.ipynb`: The Jupyter Notebook containing all data cleaning, manipulation, and plotting logic.
* `QueryResults.csv`: The raw dataset (can be refreshed via SQL query).

---

## 🚀 How to Run
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/YourUsername/stack-overflow-trends.git](https://github.com/YourUsername/stack-overflow-trends.git)
    cd stack-overflow-trends
    ```
2.  **Install Dependencies:**
    ```bash
    pip install pandas matplotlib
    ```
3.  **Run the Notebook:**
    Launch Jupyter Notebook or VS Code to run `Analysis.ipynb`.

## 🧠 What I Learned
* **Data Pivoting:** How to transform a "long" format dataset (Date, Tag, Count) into a "wide" format (Date, Java, Python, C++...) using `df.pivot()`.
* **Time Series Handling:** Converting string dates to Timestamp objects and handling missing data (`fillna`).
* **Smoothing:** Applying a **Rolling Mean** (`rolling(window=6)`) to filter out noise and visualize macro trends.

---
*This project was completed as part of the #100DaysOfCode challenge.*
