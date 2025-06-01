import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')  
driver = webdriver.Chrome(options=options)

driver.get("https://www.demoblaze.com")

time.sleep(2)
laptops_link = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_link.click()

time.sleep(2)

laptops_data = []

while True:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.select("div.card-block")  

    for item in items:
        name = item.select_one("a.hrefch").text.strip()
        price = item.select_one("h5").text.strip().replace("$", "")
        description = item.select_one("p").text.strip()

        laptops_data.append({
            "name": name,
            "price": price,
            "description": description
        })

    try:
        next_button = driver.find_element(By.ID, "next2")
        if 'disabled' in next_button.get_attribute("class"):
            break  
        next_button.click()
        time.sleep(2)
    except:
        break  

driver.quit()

with open("laptops_data.json", "w") as f:
    json.dump(laptops_data, f, indent=2)

print("Data saved to laptops_data.json")