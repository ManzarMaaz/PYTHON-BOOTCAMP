<div align="center">
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=E50914&center=true&vCenter=true&width=900&lines=Blockbuster+Budget+Analysis;Does+More+Money+%3D+More+Revenue%3F;Linear+Regression+%7C+Seaborn+%7C+Scikit-Learn;Predicting+Box+Office+Success+with+Data" />

  <p>
    <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
    </a>
    <img src="https://img.shields.io/badge/Python-3.8+-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
    <img src="https://img.shields.io/badge/Model-Linear%20Regression-orange?style=for-the-badge&logo=scikitlearn" />
  </p>

  <img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=E50914" width="100%" />

</div>

<h2 align="center">🎬 Overview</h2>

<p align="center">
  <b>Do higher film budgets actually guarantee box office gold?</b> <br>
  I scraped and analyzed data on thousands of movies to find the statistical relationship between <b>Production Budget</b> and <b>Worldwide Gross Revenue</b>.
</p>

<p align="center">
  Using historical data (pre-2018), this project explores:
  <br>
  💰 <b>ROI Analysis:</b> How many big-budget movies actually flop? <br>
  📉 <b>The Trend:</b> Has the correlation between budget and revenue changed over the decades? <br>
  🤖 <b>Prediction:</b> Can we build a Linear Regression model to predict a movie's revenue based solely on its budget?
</p>

<br>

<h2 align="center">📊 Key Insights & Visualizations</h2>

<table align="center">
  <tr>
    <td align="center" width="50%">
      <h3>📈 Budget vs. Revenue (Regression)</h3>
      <img src="https://github.com/user-attachments/assets/b4c796dd-85d3-4a97-b6d0-28aa7efd65cc" width="100%" alt="Regression Plot" />
      <p><i>Scatter plot with a Linear Regression line showing a strong positive correlation ($R^2 \approx 0.56$) for modern films.</i></p>
    </td>
    <td align="center" width="50%">
      <h3>🕰️ Old vs. New Era</h3>
      <img src="https://github.com/user-attachments/assets/25caf4aa-7ebe-4644-8a40-1c3c21af415e" width="100%" alt="Old vs New Comparison" />
      <p><i>Comparison showing that while budgets have exploded since 1970, the predictability of returns has also increased.</i></p>
    </td>
  </tr>
</table>

> **💡 The Verdict:** There is a significant positive correlation, but it's not a guarantee. Our model explains about **56%** of the variance in revenue for modern films. This means while budget matters, **44%** of success depends on other factors (Marketing, Star Power, Reviews, etc.).

<br>

<h2 align="center">⚙️ Tech Stack & Tools</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pandas,seaborn,sklearn,jupyter" />
</p>

<table align="center">
  <tr>
    <th>Category</th>
    <th>Technologies Used</th>
  </tr>
  <tr>
    <td align="center"><b>Data Processing</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Pandas-Cleaning%20%26%20Wrangling-150458?style=flat-square&logo=pandas" /></td>
  </tr>
  <tr>
    <td align="center"><b>Visualization</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Seaborn-Regression%20Plots-green?style=flat-square&logo=python" /></td>
  </tr>
  <tr>
    <td align="center"><b>Machine Learning</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Scikit_Learn-Linear%20Regression-orange?style=flat-square&logo=scikitlearn" /></td>
  </tr>
</table>

<br>

<h2 align="center">🧠 Engineering Decisions</h2>

<p align="center">
  Raw financial data is rarely ready for Machine Learning.
</p>


[Image of machine learning workflow]

```mermaid
graph LR
    A[Raw CSV] -->|Cleaning| B(Remove '$' and ',')
    B -->|Type Conversion| C[Numeric & DateTime]
    C -->|Feature Engineering| D[Decade Column]
    D -->|Split| E{Old vs New Films}
    E -->|Training| F[Linear Regression Model]
    F -->|Output| G[Revenue Prediction]

```

### 🔧 Key Techniques Used

* **Data Cleaning:** The budget data came as strings (e.g., `$1,000,000`). I implemented a cleaning pipeline to strip currency symbols and convert them to integers.
* **Feature Engineering:** I created a `Decade` column using floor division (`// 10 * 10`) on the Release Date to analyze trends over 10-year periods.
* **Modeling:** I used `scikit-learn` to fit a Linear Regression model.
* **Coefficient:** Tells us that for every extra **$1** spent on budget, we can expect roughly **$3.10** in revenue (for modern films).
* **Intercept:** The baseline revenue.


<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=E50914" width="100%" />

<h2 align="center">🚀 Getting Started</h2>

<p align="center">To run this analysis and predict movie revenue:</p>

```bash
# 1. Clone the repository
git clone [https://github.com/ManzarMaaz/movie-revenue-prediction.git](https://github.com/ManzarMaaz/movie-revenue-prediction.git)

# 2. Install requirements
pip install pandas seaborn scikit-learn

# 3. Launch Jupyter Notebook
jupyter notebook movie_analysis.ipynb

```

<div align="center">
<h3>👤 Author: Mohammed Manzar Maaz</h3>
<p>
<a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
<img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
</a>
<a href="https://github.com/ManzarMaaz">
<img src="https://img.shields.io/github/followers/ManzarMaaz?label=Follow&style=social" />
</a>
</p>
</div>
