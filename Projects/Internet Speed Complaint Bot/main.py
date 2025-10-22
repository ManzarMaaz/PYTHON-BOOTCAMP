import os
import time

import tweepy
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Load environment variables from the .env file
load_dotenv()

# Configuration Variables loaded from .env
INTERNET_PROVIDER = os.environ.get("INTERNET_PROVIDER")

# X API Credentials loaded from .env
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

PROMISED_SPEED = 30
SPEEDTEST_URL = "https://www.speedtest.net/"


class InternetSpeedBot:
    def __init__(self):
        # Create Selenium driver with the option to keep the browser open
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 90)
        self.down_speed = "0.0"
        self.up_speed = "0.0"

    def get_internet_speed(self):
        print("Opening Speedtest Website...")
        self.driver.get(SPEEDTEST_URL)

        # Handle the cookie consent banner
        try:
            time.sleep(5)
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_button.click()
        except Exception:
            print("Cookie banner not found or skipped.")
        time.sleep(5)
        # Click the 'GO' button to start the test
        start_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "js-start-test"))
        )
        start_button.click()
        print("Please wait while we calculate the Internet Speed....")

        time.sleep(70)

        download_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "download-speed"))
        )

        # CRITICAL: Wait until the element has a non-zero number (test finished)
        self.wait.until(
            lambda driver: download_element.text != ""
            and float(download_element.text) > 0.0
        )

        self.down_speed = download_element.text
        self.up_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        print("Wait is Over")
        print(f"Download Speed (Mbps): {self.down_speed}")
        print(f"Upload Speed (Mbps): {self.up_speed}")

        # Give 5 seconds for visual confirmation before quitting the browser
        time.sleep(10)
        self.driver.quit()


class TweepyClient:
    def __init__(self):
        # Initialize Tweepy Client with OAuth 1.0a credentials for posting (Write permission)
        self.client = tweepy.Client(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            wait_on_rate_limit=True,
        )

    def tweet_at_provider(self, download_speed, upload_speed):
        try:
            current_down = float(download_speed)
            current_up = float(upload_speed)
        except ValueError as e:
            print(
                f"Conversion Error: Speed details were invalid. Cannot tweet. Error: {e}"
            )
            return

        # Tweet only if either speed is less than the promised speed
        if (current_down < PROMISED_SPEED) or (current_up < PROMISED_SPEED):
            tweet = f"Hey {INTERNET_PROVIDER}, why is my internet speed {download_speed} Download Mbps & {upload_speed} Upload Mbps when I pay for {PROMISED_SPEED} Mbps Pack?"

            try:
                self.client.create_tweet(text=tweet)
                print(
                    f"✅ Tweet posted successfully. Download speed ({current_down} Mbps) is below {PROMISED_SPEED} Mbps threshold."
                )
            except Exception as e:
                print(f"❌ Error posting tweet: {e}")
        else:
            print(
                f"⏩ Speed is acceptable (Down: {current_down} Mbps). No tweet necessary."
            )


# --------------------------

# 1. Start the bot and run the speed test
speed_bot = InternetSpeedBot()
speed_bot.get_internet_speed()

# 2. Retrieve the results
download_speed = speed_bot.down_speed
upload_speed = speed_bot.up_speed

# 3. Check if speeds are valid before attempting to tweet
if float(download_speed) > 0.0 or float(upload_speed) > 0.0:
    tweepy_client = TweepyClient()
    tweepy_client.tweet_at_provider(
        download_speed=download_speed, upload_speed=upload_speed
    )
else:
    print("Tweet skipped because speed test failed to capture results.")
