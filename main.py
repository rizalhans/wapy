#reff
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip
import time

chromeDriver ='/usr/local/bin/chromedriver'
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=profile/hans")
browser = webdriver.Chrome(chromeDriver, options=chrome_options)

browser.maximize_window()

browser.get('https://web.whatsapp.com/')

with open('groups.txt', 'r', encoding='utf8') as f:
    groups = [group.strip() for group in f.readlines()]

with open('msg.txt', 'r', encoding='utf8') as f:
    msg = f.read()

for group in groups:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )

    search_box.clear()

    time.sleep(1)

    pyperclip.copy(group)

    search_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"

    time.sleep(2)

    group_xpath = '//span[@title="*BOT*"]'
    group_title = browser.find_element_by_xpath(group_xpath)

    group_title.click()

    time.sleep(1)
    
    input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
    input_box = browser.find_element_by_xpath(input_xpath)

    pyperclip.copy(msg)
    input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
    input_box.send_keys(Keys.ENTER)

    time.sleep(2)
