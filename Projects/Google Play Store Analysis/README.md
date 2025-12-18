<div align="center">
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=3DDC84&center=true&vCenter=true&width=900&lines=Google+Play+Store+Analysis;Analyzing+10,000%2B+Android+Apps;Pandas+%7C+Plotly+%7C+Data+Cleaning;Uncovering+Revenue+%26+Download+Trends" />

  <p>
    <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
    </a>
    <img src="https://img.shields.io/badge/Python-3.8+-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
    <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
  </p>

  <img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=3DDC84" width="100%" />

</div>

<h2 align="center">📱 Overview</h2>

<p align="center">
  <b>What makes an app successful on the Google Play Store?</b> <br>
  I conducted a comprehensive analysis of the Android App Market to compare thousands of apps and uncover the recipe for success.
</p>

<p align="center">
  Using a scraped dataset of over <b>10,000 apps</b>, this project explores:
  <br>
  💸 <b>Monetization:</b> How much revenue do Paid Apps actually generate? <br>
  📉 <b>The "Free" Advantage:</b> How many downloads do you lose by charging for your app? <br>
  🎮 <b>Category Dominance:</b> Which app categories have the fiercest competition?
</p>

<br>

<h2 align="center">📊 Key Insights & Visualizations</h2>

<table align="center">
  <tr>
    <td align="center" width="50%">
      <h3>📉 The "Paid" Penalty</h3>
      <img src="https://github.com/user-attachments/assets/c41ce136-e31a-4455-afd8-916ad2b8f9b6" width="100%" alt="Paid vs Free Downloads" />
      <p><i>Box plot showing the massive drop in median downloads when an app switches from Free to Paid.</i></p>
    </td>
    <td align="center" width="50%">
      <h3>☁️ Category Concentration</h3>
      <img src="https://github.com/user-attachments/assets/4cf75cf7-59f5-4745-9bd2-f6ef67352796"
 width="100%" alt="Category Scatter Plot" />
      <p><i>Scatter plot revealing that while <b>Tools</b> and <b>Entertainment</b> have many apps, <b>Photography</b> punches above its weight in downloads.</i></p>
    </td>
  </tr>
</table>

> **💡 The Verdict:** The "Game" category is the most competitive but also the most lucrative. However, for Paid Apps, the median number of installs drops precipitously compared to Free Apps, suggesting a "Freemium" model is superior for reach.

<br>

<h2 align="center">⚙️ Tech Stack & Tools</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pandas,plotly,jupyter,git,github" />
</p>

<table align="center">
  <tr>
    <th>Category</th>
    <th>Technologies Used</th>
  </tr>
  <tr>
    <td align="center"><b>Core Analysis</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Python-Pandas-150458?style=flat-square&logo=pandas" /></td>
  </tr>
  <tr>
    <td align="center"><b>Visualization</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=flat-square&logo=plotly" /></td>
  </tr>
  <tr>
    <td align="center"><b>Data Cleaning</b></td>
    <td align="center"><img src="https://img.shields.io/badge/String%20Processing-Regex-green?style=flat-square" /></td>
  </tr>
</table>

<br>

<h2 align="center">🧠 Engineering Decisions</h2>

<p align="center">
  Real-world data is messy. A significant portion of this project involved <b>Data Cleaning</b> before any analysis could begin.
</p>

```mermaid
graph LR
    A[Raw Data] -->|Drop NaN & Duplicates| B(Clean DataFrame)
    B -->|String Replace '$' & ','| C(Type Conversion)
    C -->|Calculation| D[Revenue Estimate]
    
    C --> E{Plotly Visualizations}
    D --> E

```

### 🔧 Key Techniques Used

* **Data Cleaning:** The `Installs` column was stored as strings (e.g., `"1,000,000+"`). I used string manipulation to strip special characters and convert them to integers for analysis.
* **Logarithmic Scales:** Since app downloads range from 0 to 1 Billion, standard charts were unreadable. I utilized `yaxis=dict(type='log')` in Plotly to visualize this massive variance clearly.
* **Nested Data Extraction:** The `Genres` column contained nested data (e.g., "Art;Pretend Play"). I split and stacked these values to accurately count genre popularity.

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=3DDC84" width="100%" />

<h2 align="center">🚀 Getting Started</h2>

<p align="center">To run this analysis on your local machine:</p>

```bash
# 1. Clone the repository
git clone [https://github.com/ManzarMaaz/google-play-analysis.git](https://github.com/ManzarMaaz/google-play-analysis.git)

# 2. Install requirements
pip install pandas plotly

# 3. Launch Jupyter Notebook
jupyter notebook main.ipynb

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
