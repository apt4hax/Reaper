from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import glob

def read_keywords_from_files():
    keywords = []
    for file in glob.glob('key/*.txt'):
        with open(file, 'r') as f:
            keywords.extend(f.read().splitlines())
    return keywords

def run_search(driver, query):
    print(f"Searching: {query}")
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, 'q')
    search_box.clear()
    search_box.send_keys(query)
    search_box.submit()
    time.sleep(7)
    links = set()

    while True:
        if 'sorry' in driver.current_url:
            raise Exception("Google captcha blocked the search.")

        elements = driver.find_elements(By.XPATH, '//a[@href]')
        for element in elements:
            href = element.get_attribute('href')
            if href and 'google' not in href:
                links.add(href)

        try:
            next_page = driver.find_element(By.ID, 'pnnext')
            driver.execute_script("arguments[0].click();", next_page)
            time.sleep(7)
        except:
            break

    for link in links:
        print(f"Found link: {link}")
    return links

def youdork_main(domains, dorks):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    keywords = read_keywords_from_files()
    all_links = set()

    try:
        for domain in domains:
            for dork in dorks:
                for keyword in keywords:
                    query = dork.format(domain, keyword)
                    links = run_search(driver, query)
                    all_links.update(links)
                    time.sleep(10)
    except Exception as e:
        print("Error occurred:", e)
    finally:
        driver.quit()

    print("Writing links to file...")
    with open('loot/search_results.txt', 'w') as file:
        for link in all_links:
            file.write(f"{link}\n")
    print("Done writing links.")
