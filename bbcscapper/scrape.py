from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from .models import News

options = Options()
user_agent = (
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
)
options.headless = True
options.add_experimental_option("detach", True)
options.add_argument(f"user-agent={user_agent}")
options.add_argument("--window-size=1920,1080")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--lang=en-GB")
options.add_argument("log-level=2")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
def scrapping(driver):
    driver.get('https://www.bbc.com/')
    news_cards = driver.find_elements(by=By.CSS_SELECTOR, value='.block-link__overlay-link')

    if news_cards:
        for i in range(len(news_cards)):
            link = news_cards[i].get_attribute("href")
            driver
            driver.get(link)

            try:
                title = driver.find_element(by=By.CSS_SELECTOR, value='.ssrcss-15xko80-StyledHeading')
                article_body_elements = driver.find_elements(by=By.CSS_SELECTOR, value='article .ssrcss-11r1m41-RichTextComponentWrapper')
                description = ''
                for p in article_body_elements:
                    description += p.text+'\n'

                new_record=News( title =title.text,description = description)

                new_record.save()
            except Exception as err:
                print(f"Error scraping article: {str(err)}")
                continue

    driver.close()