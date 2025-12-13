<div align="center">
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=4285F4&center=true&vCenter=true&width=900&lines=Google+Trends+Data+Analysis;Does+Search+Volume+Predict+Price%3F;Tesla+Stock+%7C+Bitcoin+%7C+Unemployment;Pandas+Time+Series+%26+Matplotlib" />

  <p>
    <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
    </a>
    <img src="https://img.shields.io/badge/Python-3.8+-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
    <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
  </p>

  <img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=4285F4" width="100%" />

</div>

<h2 align="center">📉 Overview</h2>

<p align="center">
  <b>Can Google Search volume predict the stock market or the economy?</b> <br>
  I analyzed over 15 years of data to find the correlation between <b>search popularity</b> and <b>real-world metrics</b>.
</p>

<p align="center">
  Using data from <a href="https://trends.google.com/">Google Trends</a>, <a href="https://finance.yahoo.com/">Yahoo Finance</a>, and <a href="https://fred.stlouisfed.org/">FRED</a>, this project investigates:
  <br>
  🚗 <b>Tesla:</b> Does online hype correlate with stock price? <br>
  💰 <b>Bitcoin:</b> Is crypto volatility driven by search interest? <br>
  💼 <b>Unemployment:</b> Can search data predict the unemployment rate better than the government?
</p>

<br>

<h2 align="center">📊 Key Insights & Visualizations</h2>

<table align="center">
  <tr>
    <td align="center" width="50%">
      <h3>🚗 Tesla Stock vs. Hype</h3>
      <img src="https://github.com/user-attachments/assets/3b7f757c-5b67-408d-bc7a-98cf4c63a497" width="100%" alt="Tesla Chart" />
      <p><i>Strong correlation between Search Trend (Blue) and Stock Price (Green).</i></p>
    </td>
    <td align="center" width="50%">
      <h3>💰 Bitcoin Price Volatility</h3>
      <img src="https://github.com/user-attachments/assets/d525407c-3fa5-4ab7-b6fa-5dd47567ecee" width="100%" alt="Bitcoin Chart" />
      <p><i>Search spikes often align with massive price rallies and crashes.</i></p>
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <h3>📉 Unemployment: A Leading Indicator?</h3>
      <img src="https://github.com/user-attachments/assets/b49c6630-69da-4bfe-8bd8-43ee9ccf780c" width="80%" alt="Unemployment Chart" />
      <p><i>The "Unemployment Benefits" search term (Green) often spikes <b>before</b> the official UNRATE (Red) rises, making it a valuable leading indicator.</i></p>
    </td>
  </tr>
</table>

> **💡 The Verdict:** Google Trends data is a powerful **Leading Indicator**. In the case of unemployment, search volume spiked weeks before the official government data reflected the 2020 crisis.

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
    <td align="center"><b>Data Processing</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Pandas-Resampling%20%26%20Cleaning-150458?style=flat-square&logo=pandas" /></td>
  </tr>
  <tr>
    <td align="center"><b>Visualization</b></td>
    <td align="center"><img src="https://img.shields.io/badge/Matplotlib-Twin%20Axes%20Charts-11557c?style=flat-square&logo=python" /></td>
  </tr>
</table>

<br>

<h2 align="center">🧠 Engineering Decisions</h2>

<p align="center">
  Handling disparate time-series data required robust preprocessing.
</p>

```mermaid
graph LR
    A[Daily Bitcoin Data] -->|Resample Rule='M'| B(Monthly Average)
    C[Google Trends Data] -->|Convert to Datetime| D(Time Series)
    E[FRED Unemployment] -->|Filtering| F(Clean Data)
    
    B --> G{Matplotlib TwinX}
    D --> G
    F --> G
```

🔧 Key Techniques Used

Resampling Time Series: Bitcoin price data was available daily, while Google Trends was monthly. I used df.resample('M').mean() to downsample the Bitcoin data for an accurate apple-to-apple comparison.

Dual-Axis Plotting (TwinX): Comparing "Search Volume" (0-100) with "Stock Price" ($0-$600) on one chart is impossible. I used plt.twinx() to create two independent Y-axes sharing the same X-axis (Time).

Rolling Averages: To smooth out the noise in the Unemployment search data, I applied a 6-month Rolling Average (df.rolling(window=6).mean()), which revealed the underlying trend clearer than the raw data.

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=4285F4" width="100%" />

<h2 align="center">🚀 Getting Started</h2>

<p align="center">To run this analysis on your local machine:</p>

```Bash
# 1. Clone the repository
git clone [https://github.com/ManzarMaaz/google-trends-analysis.git](https://github.com/ManzarMaaz/google-trends-analysis.git)

# 2. Install requirements
pip install pandas matplotlib

# 3. Launch Jupyter Notebook
jupyter notebook main.ipynb
```
<div align="center">
  <h3>👤 Author: Mohammed Manzar Maaz</h3>
  <p><a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" /> </a> 
    <a href="https://github.com/ManzarMaaz"> <img src="https://img.shields.io/github/followers/ManzarMaaz?label=Follow&style=social" /> </a> 
  </p> 
</div>

