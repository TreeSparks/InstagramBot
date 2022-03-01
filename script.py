import random
import time

from selenium.webdriver import Keys

from credentials import login_username, login_password, target_username
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Location of 'chromedriver.exe'
PATH = "C:\\Program Files (x86)\\chromedriver.exe"

browser = webdriver.Chrome(executable_path=PATH)

browser.get("https://www.instagram.com")

only_first = 0  # Helps prevent errors. For bad internet mainly


#  Login
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).send_keys(login_username)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))).send_keys(login_password)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
# pop-ups
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
try:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'))).click()
except Exception:
    pass
try:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]'))).click()
except Exception:
    pass

# Find target
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search"]'))).send_keys(target_username)

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]'))).click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button'))).click()

# Send message line by line in given file
with open("BasicScript.txt") as file:
    for line in file:
        msg = line
        # Send msg
        send = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
        send.send_keys(msg)
        send.send_keys(Keys.RETURN)
        # New Msg
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button'))).click()
        if only_first == 0:
            time.sleep(5)
            only_first += 1

        # Most Recent
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div[2]/div[2]/div[2]/div/div[3]/button'))).click()

        # Enter
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div[1]/div/div[2]/div/button'))).click()

        # Slows down time in between messages
        time.sleep(random.randint(1, 3))
file.close()

# Waits 5 seconds then closes program and Chrome window
time.sleep(5)
browser.quit()
