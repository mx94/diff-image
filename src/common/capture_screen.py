from selenium import webdriver
import time
from src.constant.vars import *


def capture_screen(prm):
    # mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('window-size=' + prm['window_size'])
    browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)
    print('截屏中，请稍后...')
    browser.get(prm['site_url'])
    time.sleep(2)
    browser.save_screenshot(screen_path)

    browser.quit()
