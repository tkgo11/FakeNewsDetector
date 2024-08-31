from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import re
from time import sleep
from alive_progress import alive_bar
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-gpu')
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

# Initialize files
files = {
    "사실": open("사실.txt", "w", encoding="utf-8"),
    "대체로 사실": open("대체로 사실.txt", "w", encoding="utf-8"),
    "절반의 사실": open("절반의 사실.txt", "w", encoding="utf-8"),
    "대체로 사실 아님": open("대체로 사실 아님.txt", "w", encoding="utf-8"),
    "전혀 사실 아님": open("전혀 사실 아님.txt", "w", encoding="utf-8"),
    "판단 유보": open("판단 유보.txt", "w", encoding="utf-8"),
    "논쟁 중": open("논쟁 중.txt", "w", encoding="utf-8")
}

# 웹 페이지 열기
driver.get("https://factcheck.snu.ac.kr/")
cards = None
old_cards = None
try:
    page = 1
    with alive_bar(487) as bar:
        while True:
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

            # # title과 label 텍스트 추출
            # label = "판단 유보"
            # while label == "판단 유보":
            #     for card in cards:
            #         label = card.find_element(By.CSS_SELECTOR, "div[class*='fact-dial-label-text']").text
            #         if label != "판단 유보" and label != None:
            #             break
            for card in cards:
                label = card.find_element(By.CSS_SELECTOR, "div[class*='fact-dial-label-text']").text
                title = card.find_element(By.CSS_SELECTOR, "div[class*='fact-check-title']:not([class*='fact-check-title-keyword-source-pc-container'])").text
                #print(f"title: {title}, label: {label}")
                files[label].write(title + "\n")
                files[label].flush()
                os.fsync(files[label].fileno())
            # Click pagination button
            pagination_button = WebDriverWait(driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, f"//button[contains(@class, 'page-index-button') and contains(@class, 'btn') and contains(@class, 'btn-outline-secondary') and contains(@class, 'btn-sm') and text()='{page+1}']"))
            )
            driver.execute_script("arguments[0].click();", pagination_button)
            if page == 487:
                break
            page += 1
            bar()
finally:
    for file in files.values():
        file.close()
    driver.quit()  # 브라우저 종료