from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# TODO: Maybe you could test bikesonline.com instead!!!


def test_python_successful_search():
    browser = webdriver.Chrome()
    try:
        browser.get("https://www.python.org")

        assert "Welcome to Python.org" in browser.title

        search_input = browser.find_element(By.NAME, 'q')
        search_input.clear()
        search_input.send_keys("python")
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)
        page = browser.page_source

        assert "No results found" not in page


    finally:
        browser.close()


def test_python_unsuccessful_search():
    browser = webdriver.Chrome()
    try:
        browser.get("https://www.python.org")
        assert "Welcome to Python.org" in browser.title
        search_input = browser.find_element(By.NAME, 'q')
        search_input.clear()
        search_input.send_keys("kjsfhliwhefiwufe")
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)
        page = browser.page_source
        assert "No results found" in page
    finally:
        browser.close()


if __name__ == "__main__":

    print("Hello world, program is starting...")
    time.sleep(2)

    test_python_unsuccessful_search()
    print("done.")
