# from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
#from webdriver_manager.chrome import ChromeDriverManager
from seleniumbase import Driver
import timeit




# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.

# Replace 'path/to/chromedriver' with the path to your ChromeDriver
# service = Service(executable_path=r'/Users/kireetichilakamarry/Downloads/chromedriver_mac_arm64/chromedriver')
driver = Driver(headless=True)
url = 'https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e'

while True:
    try:
        # URL of the page to scrape
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        start = timeit.default_timer()

        driver.get(url)

        # Wait for the dynamic content to load
        time.sleep(2)  # Adjust sleep time as necessary

        # Now that the page is loaded, locate the element containing the data
        # Replace 'styles_waitTimeFullnessWrapper__3PRdQ' with the correct class name if it has changed
        data_element = driver.find_element(By.CLASS_NAME, 'styles_fullness__rayxl')

        # Extract and print the data
        if data_element:
            print(data_element.text)
        else:
            print("Data not found.")

    finally:
        pass
        # driver.quit()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    driver.implicitly_wait(3)

