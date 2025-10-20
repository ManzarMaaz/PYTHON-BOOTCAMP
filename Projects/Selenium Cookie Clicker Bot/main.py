import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

GAME_URL = "http://ozh.github.io/cookieclicker/"
WAIT_TIME = 10
TIMEOUT = time.time() + WAIT_TIME
ONE_MINUTE = time.time() + (1 * 60)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(GAME_URL)

driver.maximize_window()


wait = WebDriverWait(driver, 10)
print("Waiting for Language Selection.....")

try:
    element = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#langSelect-EN"))
    ).click()
    print("Language is Selected Successfully!!!")
except Exception as e:
    print(f"Language Button Not found : {e}")

print("Searching for Big Cookie Element....")
time.sleep(1)
try:
    big_cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
    print("Big Cookie is Ready to Clickable")
except Exception as e:
    print(f"Big Cookie not found : {e}")

products_ids = [f"product{i}" for i in range(18)]  # 0 --> 17

start_time = time.time()

last_checked_time = start_time


while True:
    big_cookie.click()

    if time.time() > TIMEOUT:
        try:
            cookies_text = driver.find_element(By.ID, value="cookies").text.split(" ")
            cookies_count = int(cookies_text[0].replace(",", ""))

            products_elements = driver.find_elements(
                By.CLASS_NAME, value="product.unlocked"
            )
            products_elements.reverse()

            best_item = None

            if products_elements:
                for product in products_elements:
                    if "enabled" in product.get_attribute("class"):
                        best_item = product
                        break

                if best_item:
                    best_item.click()

                    product_name = best_item.find_element(
                        By.CLASS_NAME, "productName"
                    ).text
                    price_element = best_item.find_element(
                        By.CLASS_NAME, "price"
                    ).text.replace(",", "")

                    price = int(price_element)
                    print(f"Purchased:{product_name} at price {price}")
        except Exception as e:
            print(f"Couldnt found Cookie count or Items : {e}")

        TIMEOUT = time.time() + WAIT_TIME

    if time.time() > ONE_MINUTE:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies").text
            print(f"Final Results: {cookies_element}")
            break

        except Exception as e:
            print(f"Couldnt get final Cookie: {e}")
            break

driver.quit()
