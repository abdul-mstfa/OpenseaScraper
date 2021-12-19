from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(ChromeDriverManager().install())
DRIVER_PATH = '/path/to/chromedriver'
url="https://opensea.io/collection/terraforms"
driver.get(url)
driver.maximize_window()


def scroll_down(self):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = self.driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        #time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = self.driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height

wait = WebDriverWait(driver, 10000)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"AssetCardFooter--name")))
locations =len(driver.find_elements(By.CLASS_NAME,"AssetCardFooter--name"))
print(locations)
i= 0 
scroll = 0
for items in range(locations):
    elements = driver.find_elements(By.CLASS_NAME,"AssetCardFooter--name")
    list = driver.find_elements(By.CLASS_NAME,"AssetCardFooter--name")
    driver.execute_script("arguments[0].scrollIntoView(true);", list[scroll])
    print (elements[i].text)
    i= i+1
    scroll = scroll + 1
    print (scroll)
#for x in range(len(locations)):
"""counter = 1
for locations in locations:
    print (locations.text)

    counter+=1
    if counter==100:
        break

    driver.quit"""