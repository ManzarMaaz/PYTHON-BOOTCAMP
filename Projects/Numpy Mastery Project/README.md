<div align="center">
  
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=013243&center=true&vCenter=true&width=900&lines=NumPy+Mastery+Project;From+Vectors+to+Computer+Vision;Manipulating+Images+as+Matrices;Linear+Algebra+%7C+Broadcasting+%7C+Tensors" />

  <p>
    <a href="https://www.linkedin.com/in/mohammed-manzar-maaz">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" />
    </a>
    <img src="https://img.shields.io/badge/Python-3.8+-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
    <img src="https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy" />
  </p>

  <img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=013243" width="100%" />

</div>

<h2 align="center">🔢 Overview</h2>

<p align="center">
  <b>Images are just numbers.</b> <br>
  This project demystifies computer vision by stripping it down to its core: <b>Numerical Python (NumPy)</b>.
</p>

<p align="center">
  By treating images as <b>N-Dimensional Arrays (Tensors)</b>, we can manipulate them using pure mathematics rather than editing software. This notebook progresses from basic vector operations to complex matrix multiplication and image processing.
</p>

<br>

<h2 align="center">🎨 Visualizing Math</h2>

<table align="center">
  <tr>
    <td align="center" width="33%">
      <h3>1️⃣ The Input</h3>
      <p><i>Standard RGB Image <br> (Height x Width x 3 Channels)</i></p>
    </td>
    <td align="center" width="33%">
      <h3>2️⃣ Matrix Math</h3>
      <p><i>Matrix Multiplication <br> <code>RGB_Array @ Grey_Weights</code></i></p>
    </td>
    <td align="center" width="33%">
      <h3>3️⃣ The Output</h3>
      <p><i>Grayscale / Solarized <br> Transformed Tensor</i></p>
    </td>
  </tr>
  <tr>
    <td colspan="3" align="center">
      <img src="https://github.com/user-attachments/assets/578f36b3-6a4b-4cca-a07a-3bf9d292ca07" width="100%" alt="Image Manipulation Demo" />
    </td>
  </tr>
</table>

> **💡 The Concept:** A color image is just a stack of three matrices (Red, Green, Blue). By manipulating these matrices using linear algebra, we can perform filters, rotations, and inversions instantly.



<br>

<h2 align="center">🧠 Key Concepts Covered</h2>

### 📐 1. N-Dimensional Arrays (ndarrays)
We explore the hierarchy of data structures in NumPy:
* **Vectors (1D):** Simple lists of numbers (e.g., Sound waves).
* **Matrices (2D):** Spreadsheets or Grayscale images.
* **Tensors (3D+):** Color images (RGB) or Video data.

### ⚡ 2. Broadcasting & Linear Algebra
Using linear algebra to process data without slow `for` loops.


* **Broadcasting:** Adding a scalar to a matrix (e.g., brightening an image).
* **Matrix Multiplication:** Using the `@` operator or `.matmul()` for dot products.

### 🖼️ 3. Image Processing
Converting math into visual results:
* **Grayscale Conversion:** Calculating the dot product of RGB channels with specific weights (`[0.2126, 0.7152, 0.0722]`) to mimic human eye perception.
* **Solarization:** Inverting colors mathematically (`255 - image_array`).

<br>

<h2 align="center">⚙️ Tech Stack & Tools</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,numpy,matplotlib,vscode,git" />
</p>

<table align="center">
  <tr>
    <th>Library</th>
    <th>Use Case</th>
  </tr>
  <tr>
    <td align="center"><b>NumPy</b></td>
    <td align="center">High-performance array manipulation and linear algebra.</td>
  </tr>
  <tr>
    <td align="center"><b>Matplotlib</b></td>
    <td align="center">Visualizing data distributions and rendering images from arrays.</td>
  </tr>
  <tr>
    <td align="center"><b>SciPy / PIL</b></td>
    <td align="center">Loading real-world image datasets (`face`, `misc`).</td>
  </tr>
</table>

<br>

<h2 align="center">🚀 Getting Started</h2>

<p align="center">To run this notebook locally:</p>

```bash
# 1. Clone the repository
git clone [https://github.com/ManzarMaaz/numpy-image-processing.git](https://github.com/ManzarMaaz/numpy-image-processing.git)

# 2. Install requirements
pip install numpy matplotlib scipy pillow

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
