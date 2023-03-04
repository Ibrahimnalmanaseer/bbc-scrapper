from apscheduler.schedulers.background import BackgroundScheduler
from .scrape import scrapping,options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrapping, 'interval', hours=1,args=[webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)])
    scheduler.start()