from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import re
from time import sleep
from tqdm import tqdm
import threading

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-gpu')
options.add_argument("--incognito")

# Initialize files
files = {
    "사실": open("data/사실.txt", "w", encoding="utf-8"),
    "대체로 사실": open("data/대체로 사실.txt", "w", encoding="utf-8"),
    "절반의 사실": open("data/절반의 사실.txt", "w", encoding="utf-8"),
    "대체로 사실 아님": open("data/대체로 사실 아님.txt", "w", encoding="utf-8"),
    "전혀 사실 아님": open("data/전혀 사실 아님.txt", "w", encoding="utf-8"),
    "판단 유보": open("data/판단 유보.txt", "w", encoding="utf-8")
}

def process_page(driver, page):
    driver.get(f"https://factcheck.snu.ac.kr/?page={page}")
    cards_container = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class*='fact-check-cards-container']")),
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class*='fact-dial-needle']"))
    )
    cards = cards_container.find_elements(By.CSS_SELECTOR, "div[class*='jsx-18931043 fact-check-card-container']")

    for card in cards:
        label = card.find_element(By.CSS_SELECTOR, "div[class*='fact-dial-label-text']").text
        title = card.find_element(By.CSS_SELECTOR, "div[class*='fact-check-title']:not([class*='fact-check-title-keyword-source-pc-container'])").text
        files[label].write(title + "\n")

def process_pages(bar, driver, start_page, end_page):
    for page in range(start_page, end_page+1):
        process_page(driver, page)
        bar.update(1)

def main():
    total_pages = 487  # Set total pages here
    num_threads = 5  # Set number of threads here
    pages_per_thread = total_pages // num_threads  # Calculate pages per thread

    threads = []
    drivers = []  # List to store driver objects
    bar = tqdm(total=total_pages)  # Track progress of total pages
    for i in range(num_threads):  # Create threads
        start_page = i * pages_per_thread + 1
        end_page = (i + 1) * pages_per_thread
        if i == num_threads - 1:  # Last thread should process remaining pages
            end_page = total_pages

        driver = webdriver.Chrome(options=options)
        drivers.append(driver)  # Store the driver object
        thread = threading.Thread(target=process_pages, args=(bar, driver, start_page, end_page))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for file in files.values():
        file.close()
    for driver in drivers:  # Close the drivers
        driver.quit()  # 브라우저 종료
if __name__ == "__main__":
    main()