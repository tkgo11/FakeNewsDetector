from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import re
from time import sleep
from alive_progress import alive_bar
import os
import threading
from tqdm import tqdm
import requests

#I think using requests is better than selenium, but idk how to do that
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-gpu')
options.add_argument("--incognito")

files = {
    "사실": open("data/사실.txt", "w", encoding="utf-8"),
    "대체로 사실": open("data/대체로 사실.txt", "w", encoding="utf-8"),
    "절반의 사실": open("data/절반의 사실.txt", "w", encoding="utf-8"),
    "대체로 사실 아님": open("data/대체로 사실 아님.txt", "w", encoding="utf-8"),
    "전혀 사실 아님": open("data/전혀 사실 아님.txt", "w", encoding="utf-8"),
    "판단 유보": open("data/판단 유보.txt", "w", encoding="utf-8"),
    "논쟁 중": open("data/논쟁 중.txt", "w", encoding="utf-8")
}

def single_threaded_process():
    driver = webdriver.Chrome(options=options)
    driver.get("https://factcheck.snu.ac.kr/")
    cards = None
    old_cards = None
    try:
        page = 1
        with alive_bar(487) as bar:
            while True:
                bar()
                while old_cards == cards:
                    cards_container = WebDriverWait(driver, 10).until(
                        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class*='fact-check-cards-container']")),
                    )
                    cards = cards_container.find_elements(By.CSS_SELECTOR, "div[class*='jsx-18931043 fact-check-card-container']")
                
                WebDriverWait(driver, 10).until(
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "img[class*='fact-dial-needle']"))
                )
                cards_container = WebDriverWait(driver, 10).until(
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class*='fact-check-cards-container']")),
                )
                cards = cards_container.find_elements(By.CSS_SELECTOR, "div[class*='jsx-18931043 fact-check-card-container']")
                old_cards = cards

                for card in cards:
                    label = card.find_element(By.CSS_SELECTOR, "div[class*='fact-dial-label-text']").text
                    title = card.find_element(By.CSS_SELECTOR, "div[class*='fact-check-title']:not([class*='fact-check-title-keyword-source-pc-container'])").text
                    files[label].write(title + "\n")
                    files[label].flush()
                    os.fsync(files[label].fileno())
                pagination_button = WebDriverWait(driver, 10).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, f"//button[contains(@class, 'page-index-button') and contains(@class, 'btn') and contains(@class, 'btn-outline-secondary') and contains(@class, 'btn-sm') and text()='{page+1}']"))
                )
                driver.execute_script("arguments[0].click();", pagination_button)
                if page == 487:
                    break
                page += 1
    finally:
        for file in files.values():
            file.close()
        driver.quit()

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

def multi_threaded_process():
    total_pages = 487
    num_threads = 5
    pages_per_thread = total_pages // num_threads

    threads = []
    drivers = []
    bar = tqdm(total=total_pages)
    for i in range(num_threads):
        start_page = i * pages_per_thread + 1
        end_page = (i + 1) * pages_per_thread
        if i == num_threads - 1:
            end_page = total_pages

        driver = webdriver.Chrome(options=options)
        drivers.append(driver)
        thread = threading.Thread(target=process_pages, args=(bar, driver, start_page, end_page))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for file in files.values():
        file.close()
    for driver in drivers:
        driver.quit()

if __name__ == "__main__":
    server_url = "https://factcheck.snu.ac.kr"
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            print(f"Server at {server_url} is up and running.")
        else:
            print(f"Server at {server_url} returned status code {response.status_code}.")
            print("Exiting...")
            exit()
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to {server_url}. Error: {e}")
        print("Exiting...")
        exit()
    choice = input("Choose mode: (1) Single-threaded, (2) Multi-threaded: ")
    if choice == '1':
        single_threaded_process()
    elif choice == '2':
        print("Multi-threaded mode is not implemented yet. Plz contribute to the project.")
        #multi_threaded_process()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        print("Exiting...")
        exit()