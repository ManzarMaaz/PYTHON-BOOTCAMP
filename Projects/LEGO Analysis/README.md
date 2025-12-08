<div align="center">
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=7F5CFF&center=true&vCenter=true&width=900&lines=LEGO+Data+Analysis+Project;70+Years+of+History+Analyzed;Pandas+%7C+Matplotlib+%7C+Data+Visualization;Discovering+Trends+in+Complexity+%26+Strategy" />

  <p>
    <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
    </a>
    <img src="https://img.shields.io/badge/Python-3.8+-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
    <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
  </p>

  <img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=7F5CFF" width="100%" />

</div>

<h2 align="center">🧩 Overview</h2>

<p align="center">
  <b>Are LEGO sets getting harder to build, or are we just getting older?</b> <br>
  I put nostalgia aside and used Python to analyze over <b>70 years of LEGO history</b> (1949–2020).
</p>

<p align="center">
  Using a relational dataset sourced from Rebrickable, this project explores:
  <br>
  🚀 <b>Strategy Shift:</b> When did LEGO switch to mass licensing (Star Wars, Marvel)? <br>
  📈 <b>Complexity:</b> Have sets actually become more difficult to build? <br>
  🏆 <b>Dominance:</b> Which themes have driven the most sales volume historically?
</p>

<br>

<h2 align="center">📊 Key Insights & Visualizations</h2>

<table align="center">
  <tr>
    <td align="center" width="50%">
      <h3>📉 The Rise in Complexity</h3>
      <img src="https://github.com/user-attachments/assets/bec499a4-58f8-4df0-9001-1741393336ef" width="100%" alt="Complexity Scatter Plot" />
      <p><i>Scatter plot revealing that the average <b>parts-per-set</b> has skyrocketed since the 1980s.</i></p>
    </td>
    <td align="center" width="50%">
      <h3>💥 The Explosion of Themes</h3>
      <img src="https://github.com/user-attachments/assets/e2817fb1-30f3-46c6-af6c-9299656c6de2" width="100%" alt="Dual Axis Chart" />
      <p><i>Dual-axis chart showing the correlation between new <b>Themes</b> (Blue) and <b>Set releases</b> (Green).</i></p>
    </td>
  </tr>
</table>

> **💡 The Verdict:** The mid-1990s marked a pivotal shift in LEGO's strategy. They moved from <10 themes/year to over 80+ themes/year, coinciding with the introduction of licensed IP like *Star Wars*.

<br>

<h2 align="center">⚙️ Tech Stack & Tools</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pandas,matplotlib,jupyter,git,github" />
</p>

<table align="center">
  <tr>
    <th>Category</th>
    <th>Technologies Used</th>
  </tr>
  <tr>
    <td align="center"><b>Core Logic</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Python-3.10-blue?style=flat-square" /></td>
  </tr>
  <tr>
    <td align="center"><b>Data Manipulation</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Pandas-Grouping%20%26%20Merging-150458?style=flat-square&logo=pandas" /></td>
  </tr>
  <tr>
    <td align="center"><b>Visualization</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Matplotlib-Dual%20Axis%20Charts-11557c?style=flat-square&logo=python" /></td>
  </tr>
  <tr>
    <td align="center"><b>Environment</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Jupyter-Interactive%20Notebook-orange?style=flat-square&logo=jupyter" /></td>
  </tr>
</table>

<br>

<h2 align="center">🧠 Data Pipeline & Methodology</h2>

<p align="center">
  Unlike a simple CSV file, this data was distributed across multiple relational tables.<br>
  I reconstructed the database schema using <b>Pandas Joins</b>.
</p>

```mermaid
graph LR
    A[sets.csv] -->|Group By Year| B(Aggregated Time Series)
    C[themes.csv] -->|Merge on Theme_ID| D(Relational DataFrame)
    E[colors.csv] -->|Value Counts| F(Color Distribution)
    
    B --> G{Visualizations}
    D --> G
    F --> G
````

### 🔧 Key Engineering Decisions

  * **Handling Incomplete Data:** The dataset contained partial data for 2021. I used list slicing (`[:-2]`) to programmatically exclude incomplete years, ensuring the trend lines remained accurate.
  * **Dual-Axis Plotting:** Since *Number of Sets* and *Number of Themes* operate on vastly different scales, I utilized `plt.twinx()` to map them on the same chart without distortion.

<br>
<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=7F5CFF" width="100%">
<h2 align="center">🚀 Getting Started</h2>
<p align="center">To run this analysis on your local machine:</p>

```bash
# 1. Clone the repository
git clone [https://github.com/ManzarMaaz/lego-analysis.git](https://github.com/ManzarMaaz/lego-analysis.git)

# 2. Install requirements
pip install pandas matplotlib

# 3. Launch Jupyter Notebook
jupyter notebook lego_analysis.ipynb
```

<div align="center">
  <h3>👤 Author: Mohammed Manzar Maaz</h3>
  <p>
    <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" \>
    </a>
    <a href="https://github.com/ManzarMaaz">
      <img src="https://img.shields.io/github/followers/ManzarMaaz?label=Follow&style=social" \>
    </a>
  </p>
</div>
