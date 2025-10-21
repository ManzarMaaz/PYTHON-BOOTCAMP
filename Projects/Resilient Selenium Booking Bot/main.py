import os
import random  # Used for random delay during retry
import time

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# --- CONFIGURATION & SETUP ---
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASS = "password123"
URL = "https://appbrewery.github.io/gym/"
# CRITICAL CHANGE: Set a low timeout (e.g., 3s) for WebDriverWait
# so network failures cause a fast TimeoutException for the retry wrapper.
RETRY_TIMEOUT = 3


# --- RETRY WRAPPER FUNCTION ---
def retry(func, retries=7, description="Action"):
    """Wrapper function to retry another function up to a maximum number of times."""
    for attempt in range(1, retries + 1):
        try:
            result = func()
            print(f"✅ {description} successful on attempt {attempt}/{retries}.")
            return result
        except (
            TimeoutException,
            NoSuchElementException,
            StaleElementReferenceException,
        ):
            if attempt == retries:
                print(f"❌ {description} failed after {retries} attempts. Giving up.")
                raise  # Re-raise the final exception
            else:
                print(
                    f"🔄 {description} failed on attempt {attempt}/{retries}. Retrying..."
                )
                # Add a short, random delay for robustness
                time.sleep(1 + random.random() * 0.5)
    return None


# --- SELENIUM ACTION FUNCTIONS ---


def perform_login(driver, wait, email, password):
    """Handles the entire login process using explicit waits."""

    def attempt_login():
        # 1. Click Login Button
        login_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "Home_heroButton__3eeI3"))
        )
        login_button.click()

        # 2. Enter Credentials
        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-input")))
        email_input.clear()
        email_input.send_keys(email)

        # Note: No need for wait here if the element is already present
        pass_input = driver.find_element(By.ID, value="password-input")
        pass_input.clear()
        pass_input.send_keys(password, Keys.ENTER)

        # 3. Verification: Wait for a post-login element (schedule) to load
        # This confirms the server accepted the login, even with 50% failure rate.
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^='day-group-']"))
        )
        return True

    return retry(attempt_login, retries=5, description="Login")


def perform_booking_action(button):
    """
    Function to click the button and wait for its text to change.
    Success criterion is the text changing to 'Booked' or 'Waitlisted'.
    """

    def attempt_click_and_verify():
        # 1. Click the button
        button.click()

        # 2. Verify: Wait for the button text to change to indicate success.
        # This is the single, crucial line that makes the booking action resilient.
        wait.until(lambda d: button.text in ["Booked", "Waitlisted"])
        return button.text

    return retry(attempt_click_and_verify, retries=5, description="Class Action")


def get_my_bookings_cards(driver, wait):
    """Navigates to My Bookings page and retrieves the booking cards."""

    def attempt_get_bookings():
        # 1. Click the 'My Bookings' link
        my_bookings_link = driver.find_element(By.ID, value="my-bookings-link")
        my_bookings_link.click()

        # 2. Wait for the booking cards to appear
        wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "MyBookings_bookingCard__VRdrR")
            )
        )

        # 3. Retrieve the confirmed bookings
        confirmed_bookings = driver.find_elements(
            By.CLASS_NAME, value="MyBookings_bookingCard__VRdrR"
        )

        if not confirmed_bookings:
            # If the class name is present but no cards, something is wrong.
            raise NoSuchElementException("Booking page loaded, but no cards found.")
        return confirmed_bookings

    return retry(attempt_get_bookings, retries=5, description="Retrieve My Bookings")


# --- MAIN EXECUTION START ---

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
# Initialize wait with the low timeout for fast retries
wait = WebDriverWait(driver, RETRY_TIMEOUT)

try:
    # 1. RESILIENT LOGIN
    perform_login(driver, wait, ACCOUNT_EMAIL, ACCOUNT_PASS)
    print("✅ Logged in Successfully !!!\n")

    # Give a short buffer time after login success
    time.sleep(1)

    # Refresh schedule cards after successful login
    schedule = driver.find_elements(By.CSS_SELECTOR, value="div[id^='class-card-']")

    # Booking Summary (Keep your original counters)
    classes_booked = 0
    waitlist_joined = 0
    already_booked_waitlisted = 0
    total_classes_processed = 0
    detailed_class_list = []

    # 2. RESILIENT BOOKING LOOP
    for card in schedule:
        day_group = card.find_element(
            By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]"
        )
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        if "tue" in day_title.lower() or "thu" in day_title.lower():
            time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

            if "6:00 PM" in time_text:
                class_name = card.find_element(
                    By.CSS_SELECTOR, "h3[id^='class-name-']"
                ).text
                button = card.find_element(
                    By.CSS_SELECTOR, "button[id^='book-button-']"
                )

                print(
                    f"\n--- Processing: {class_name} on {day_title} ({time_text}) ---"
                )

                total_classes_processed += 1

                current_button_text = button.text

                if current_button_text in ["Booked", "Waitlisted"]:
                    print(
                        f"✅ Already {current_button_text}: {class_name} on {day_title}\n"
                    )
                    already_booked_waitlisted += 1

                elif current_button_text in ["Book Class", "Join Waitlist"]:
                    # Call the resilient action function
                    final_status = perform_booking_action(button)

                    if final_status == "Booked":
                        print(f"✅ Successfully Booked: {class_name} on {day_title}\n")
                        classes_booked += 1
                        detailed_class_list.append(
                            f"[New Bookings] {class_name} on {day_title}"
                        )

                    elif final_status == "Waitlisted":
                        print(f"✅ Joined Waitlist: {class_name} on {day_title}\n")
                        waitlist_joined += 1
                        detailed_class_list.append(
                            f"[New Waitlist] Entries: {class_name} on {day_title}"
                        )

    # 3. SUMMARY
    print("-------BOOKING SUMMARY--------")
    print(f"New Bookings: {classes_booked}")
    print(f"New Waitlist Entries: {waitlist_joined}")
    print(f"Already Booked/ Waitlisted: {already_booked_waitlisted}")
    print(f"Total Tuesday & Thursday 6pm classes: {total_classes_processed}\n")

    print("-------DETAILED CLASS LIST--------")
    for item in detailed_class_list:
        print(f"- {item}")

    # 4. RESILIENT VERIFICATION
    confirmed_bookings = get_my_bookings_cards(driver, wait)

    print("\n-------Verifying on my Bookings Page----")
    # You must count only the successfully booked/waitlisted items for verification
    expected_total = classes_booked + waitlist_joined

    for x in confirmed_bookings:
        class_name = x.find_element(By.TAG_NAME, value="h3")
        print(f"✅ Verified: {class_name.text}")

    print(f"\nExpected Bookings (New/Waitlist): {expected_total}")
    print(f"Found Bookings: {len(confirmed_bookings)}\n")

    if expected_total == len(confirmed_bookings):
        print("✅SUCCESS: All Bookings verified !!!")
    else:
        print(
            f"❌MISMATCH: Missing {expected_total - len(confirmed_bookings)} Bookings"
        )

except Exception as e:
    print(f"\n🚨 A critical error occurred and the bot stopped: {e}")

finally:
    time.sleep(5)
    # driver.quit()
