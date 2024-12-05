from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

task_time = time.time() + 20
upgrade_time = time.time() + 5


# Process of clicking and checking upgrade continuously
while True:
    cookie.click()

    # Check for upgrade and if found apply the highest upgrade every 5 sec
    if time.time() > upgrade_time:
        price_list = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        price_list = price_list[:-1]
        price_dict = {price.text.split()[0]: (int(price.text.split()[-1].replace(',','').strip()),price) for price in price_list}
        price_dict = dict(sorted(price_dict.items(), key=lambda item: item[1][0], reverse=True))
        current_cookies = int(driver.find_element(By.ID, value="money").text.replace(',','').strip())
        for upgrade in price_dict:
            if current_cookies >= price_dict[upgrade][0]:
                price_dict[upgrade][1].click()
                break

        upgrade_time = time.time() + 5

    # Run whole program for 5 min
    if time.time() > task_time:
        break

# Print click rate
click_rate = driver.find_element(By.ID, value="cps").text
print(f"Cookies per sec: {click_rate}")

driver.quit()



