# 🧱 LEGO Data Analysis: 70 Years of Trends
<p align="center">
  <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin" alt="Connect on LinkedIn">
  </a>
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas" alt="Pandas">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg?logo=python" alt="Matplotlib">
</p>

## 📖 Overview
This project is an exploratory data analysis (EDA) of the LEGO company's history from **1949 to 2020**.

Using a relational dataset sourced from Rebrickable, I aimed to answer specific business questions about LEGO's strategy:
1.  **Strategy Shift:** When did LEGO shift from a few core products to mass licensing (Star Wars, Marvel)?
2.  **Product Complexity:** Have sets actually become more difficult to build over time, or is it just nostalgia?
3.  **Theme Dominance:** Which themes have driven the most sales volume historically?

---

## 📊 Key Visualizations & Insights

| **The Explosion of Themes** | **The Rise in Complexity** |
|:---:|:---:|
|<img width="100%" alt="Dual Axis Chart" src="https://github.com/user-attachments/assets/0a7e5f84-c818-44cf-b51e-d9c3da70306d"   />| <img src="https://github.com/user-attachments/assets/cf13afa5-2163-43e3-85b2-7a81e2fcdba8" width="100%" alt="Complexity Scatter" /> |
| *Dual-axis chart showing the correlation between new Themes (Blue) and Set releases (Green).* | *Scatter plot revealing the average parts-per-set increasing significantly post-1980.* |

> **Key Finding:** The mid-1990s marked a pivotal shift in LEGO's strategy, moving from <10 themes/year to over 80+ themes/year, coinciding with their move into licensed IP (Star Wars, Harry Potter).

---

## ⚙️ Data Pipeline & Methodology

Unlike a flat Excel file, this data was distributed across multiple relational tables. I used **Pandas** to reconstruct the schema.

```mermaid
graph LR
    A[sets.csv] -->|Group By Year| B(Aggregated Time Series)
    C[themes.csv] -->|Merge on Theme_ID| D(Relational DataFrame)
    E[colors.csv] -->|Value Counts| F(Color Distribution)
    
    B --> G{Visualizations}
    D --> G
    F --> G
````

### 🧠 Analytical Decisions (The "Why")

  * **Handling Incomplete Data:** The dataset contained partial data for 2021. To prevent a misleading "drop-off" in the line charts, I used list slicing (`[:-2]`) to programmatically exclude incomplete years from the visualization, ensuring the trend lines remained accurate.

  * **Dual-Axis Plotting:** The number of *Sets* (700+) and *Themes* (90+) operate on vastly different scales. Plotting them on a single y-axis made the Theme data look like a flat line. I utilized `plt.twinx()` to create a secondary y-axis, allowing both trends to be visible and comparable on the same chart.

  * **Relational Merging:** To find the most popular themes, I couldn't just count rows in the `sets` table because it only contained IDs (e.g., `theme_id: 158`). I performed a database-style `JOIN` (using `pd.merge`) to link `sets.csv` with `themes.csv`, revealing that **Star Wars** is among the top themes historically.

-----

## 🛠️ Tech Stack

| Component | Technology | Use Case |
| :--- | :--- | :--- |
| **Language** | Python 3.10 | Core programming. |
| **Data Manipulation** | Pandas | Merging DataFrames, GroupBy aggregations, Data Cleaning. |
| **Visualization** | Matplotlib | Generating Line Charts, Scatter Plots, and Bar Graphs. |
| **Environment** | Jupyter Notebook | Interactive code execution and documentation. |

-----

## 🚀 Getting Started

**Clone the Repo**

```bash
git clone [https://github.com/ManzarMaaz/lego-analysis.git](https://github.com/ManzarMaaz/lego-analysis.git)
```

**Install Requirements**

```bash
pip install pandas matplotlib
```

**Run the Notebook**
Launch Jupyter Lab or Notebook to view the interactive analysis:

```bash
jupyter notebook lego_analysis.ipynb
```

-----

**Author:** [Mohammed Manzar Maaz](https://www.google.com/url?sa=E&source=gmail&q=https://www.linkedin.com/in/mohammed-manzar-maaz)
