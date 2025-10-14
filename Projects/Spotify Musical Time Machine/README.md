# 🎵 Spotify Musical Time Machine

This Python script is a musical time capsule that lets you travel back to any date and listen to the top songs of that day. It scrapes the UK's Official Singles Chart for a date you provide, then automatically creates a private Spotify playlist with all the hits from that week.



---

## ✨ Features

-   **Go Back in Time**: Input any date (year, month, day) to generate a playlist from the past.
-   **Web Scraping**: Uses `requests` and `BeautifulSoup` to scrape the top 100 songs from the Official UK Charts website.
-   **Accurate Song Matching**: Searches for each song on Spotify by **track name and year** to find the correct version.
-   **Automated Playlist Creation**: Automatically creates a new, private Spotify playlist in your account, named with the date you chose.
-   **Real-time Feedback**: Prints the status of each song search directly to the console as it runs.
-   **Robust Error Handling**: Gracefully skips songs that can't be found on Spotify and prints a notification, ensuring the script completes successfully.

---

## ⚙️ How It Works

1.  **User Input**: The script prompts you to enter a year, month, and day.
2.  **Scrape the Charts**: It constructs a URL for the Official Singles Chart for the specified date and fetches the HTML content.
3.  **Parse Song Titles**: `BeautifulSoup` parses the HTML to find and extract the list of the top 100 song titles for that week.
4.  **Authenticate with Spotify**: The script uses `spotipy` with SpotifyOAuth to securely authenticate with your Spotify account. The first time you run it, you will be prompted to log in and grant permission.
5.  **Find Song URIs on Spotify**: It iterates through the scraped song list and uses the Spotify API to search for each track's unique **URI**.
6.  **Create and Populate Playlist**: Finally, it creates a new private playlist in your Spotify account and adds all the found song URIs to it in a single, efficient API call.

---

## 🚨 Important Security Notice

This script requires your Spotify `CLIENT_ID` and `CLIENT_SECRET` to be placed directly in the code.

**⚠️ This is a security risk.** For personal use, it's acceptable, but you should **NEVER** commit your real credentials to a public Git repository. For a more secure approach, load these values from environment variables using a library like `python-dotenv`.

---

## 🛠️ Technology Stack

-   **Language**: Python 3
-   **Libraries**:
    -   `requests`: For making HTTP requests to the charts website.
    -   `beautifulsoup4`: For parsing the HTML and extracting song data.
    -   `spotipy`: A Python client for the Spotify Web API.

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.x installed.
-   A Spotify account (Free or Premium).
-   A Spotify for Developers account to get API credentials.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/spotify-time-machine.git](https://github.com/your-username/spotify-time-machine.git)
    cd spotify-time-machine
    ```

2.  **Install the required packages:**
    ```bash
    pip install requests beautifulsoup4 spotipy
    ```

3.  **Set up your Spotify Developer App:**
    -   Go to the Spotify Developer Dashboard and log in.
    -   Click "Create App". Give it a name and description.
    -   Once created, you will see your Client ID and Client Secret.
    -   Click "Edit Settings". In the "Redirect URIs" field, add `https://example.com` and click "Save". This step is crucial.

4.  **Configure the script:**
    -   Open the `main.py` file.
    -   Replace the placeholder values for `CLIENT_ID` and `CLIENT_SECRET` with the credentials from your Spotify Developer App.
    -   In the `SpotifyOAuth` call, change the `username` to your own Spotify username.

### Usage

Run the script from your terminal and follow the prompts:

```bash
python main.py
```

The script will ask for a date, then show its progress as it finds each song, and finally, create the playlist in your Spotify account.

Example Console Output:
```bash
...
Song name: SOUND OF THE UNDERGROUND, Song uri: spotify:track:0SKjqIViHaXWhmaKuJbMrq
Song name: CHEEKY SONG (TOUCH MY BUM), Song uri: spotify:track:6MCovnA5m16hln36lk0gqM
Song Not Found: SACRED TRUST/AFTER YOU'RE GONE
Song name: SORRY SEEMS TO BE THE HARDEST WORD, Song uri: spotify:track:15iPQnhXcy5R3p90MbsOxe
...
Creating Playlist : 2003-01-01 UK's Official Top 100 singles chart
Adding 66 Songs to 2003-01-01 UK's Official Top 100 singles chart Playlist....
66 Songs Successfully added to the Playlist !!!
```
