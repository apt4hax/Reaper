from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def linkedin_login(driver, username, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(5)
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    password_field.submit()
    time.sleep(5)

def scroll_and_extract_info(driver, url):
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                show_more_button = driver.find_element(By.CLASS_NAME, 'artdeco-button__text')
                show_more_button.click()
                time.sleep(5)
            except:
                break
        last_height = new_height

    user_info = []
    elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'artdeco-entity-lockup__content')]")
    for element in elements:
        try:
            name_element = element.find_element(By.XPATH, ".//div[contains(@class, 'org-people-profile-card__profile-title')]")
            title_element = element.find_element(By.XPATH, ".//div[contains(@class, 'lt-line-clamp--multi-line')]")
            name = name_element.text if name_element else 'Unknown'
            title = title_element.text if title_element else 'Unknown'
            user_info.append((name, title))
        except:
            continue
    return user_info

def lottali_main(linkedin_username, linkedin_password, company_url):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        linkedin_login(driver, linkedin_username, linkedin_password)
        user_info = scroll_and_extract_info(driver, company_url)

        #os.makedirs('key/raw', exist_ok=True)
        os.makedirs('key', exist_ok=True)

        with open('key/user-title.txt', 'w', encoding='utf-8') as file:
            for name, title in user_info:
                file.write(f"{name} - {title}\n")

        with open('key/employeeNames.txt', 'w', encoding='utf-8') as file:
            for name, _ in user_info:
                file.write(f"{name}\n")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

