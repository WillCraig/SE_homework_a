from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

WEBSITE = "https://www.bikesonline.com"


def test_successful_search():
    browser = webdriver.Chrome()
    try:
        browser.get(WEBSITE)

        assert "Bikes Online | Best Online Bicycle Shop USA" in browser.title

        search_input = browser.find_element(By.NAME, 'kw')
        search_input.clear()

        search_input.send_keys("road bike")
        search_input.send_keys(Keys.RETURN)

        # wait for the search to complete.
        time.sleep(5)

        page = browser.page_source

        assert "No results found" not in page

        sample = browser.find_element(By.CLASS_NAME, "findify-components-common--grid")

        # number of times "Road Bike" appears in search area,
        rb_str_occurrence: int = sample.text.count("Road Bike")

        # indicate whether there are more than 5 occurrences of the term "Road Bike" in the search results.
        assert rb_str_occurrence > 5



    finally:
        browser.close()


def test_button_press():

    browser = webdriver.Chrome()
    try:
        browser.get(WEBSITE)

        assert "Bikes Online | Best Online Bicycle Shop USA" in browser.title

        time.sleep(3)

        lm_button = browser.find_element(By.CLASS_NAME, "main-direct-button")

        try:
            lm_button.click()
        except:
            print('error')

        lm_button.click()

        time.sleep(5)

        assert "Learn More About Us | Bikes Online" in browser.title


    finally:
        browser.close()


if __name__ == "__main__":
    print("Hello world, program is starting...")
    time.sleep(2)

    test_successful_search()

    time.sleep(5)

    test_button_press()

    print("done.")
