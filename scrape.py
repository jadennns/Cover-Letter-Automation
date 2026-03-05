from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import re

def scrape_job(url: str) -> str:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("User-Agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(3)  # wait for JS to render
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        text = soup.get_text(separator="\n")
        return re.sub(r'\n{3,}', '\n\n', text).strip()[:6000]
    finally:
        driver.quit()
