# 🎬 Top 100 Movies Web Scraper

This is a simple yet effective Python script that scrapes the "100 Best Movies of All Time" from an archived Empire Online webpage. It extracts the movie titles, orders them from 1 to 100, and saves the list to a text file.


---

## ✨ Features

-   **Web Scraping**: Fetches HTML content from a specific URL using the `requests` library.
-   **HTML Parsing**: Efficiently parses the HTML to find and extract specific data using `BeautifulSoup`.
-   **Data Cleaning**: Isolates and extracts only the movie titles from the relevant HTML tags.
-   **File Output**: Saves the final, ordered list of 100 movies to a `top100movies.txt` file for easy access.

---

## ⚙️ How It Works

1.  **Fetch Webpage**: The script sends an HTTP GET request to a specific archived URL on the Wayback Machine that hosts the movie list.
2.  **Parse HTML**: The raw HTML from the webpage is parsed into a `BeautifulSoup` object, which allows for easy navigation and searching of the document's structure.
3.  **Find Movie Titles**: The script specifically searches the parsed HTML for all `<h3>` tags that have a `class` attribute of `title`, as these tags contain the movie titles.
4.  **Extract and Store**: The text content of each found tag is extracted and appended to a Python list.
5.  **Order and Save**: The original list on the website is ranked from 100 down to 1. The script programmatically reverses this list to get the correct 1-100 order and then writes each movie title to a new line in the `top100movies.txt` file.

---

## 🛠️ Technology Stack

-   **Language**: Python 3
-   **Libraries**:
    -   `requests`: For making HTTP requests to the URL.
    -   `BeautifulSoup4` (`bs4`): For parsing the HTML document and extracting data.

---

## 🚀 Getting Started

### Prerequisites

-   You must have Python 3.x installed on your system.

### Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Install the required packages:**
    ```bash
    pip install requests beautifulsoup4
    ```

3.  **Run the script from your terminal:**
    ```bash
    python main.py
    ```

---

## 📄 Output

After running the script, a file named `top100movies.txt` will be created in the same directory. It will contain the list of movies, ranked from 1 to 100.

**Example `top100movies.txt`:**
```text
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
5) Pulp Fiction
...and so on.
