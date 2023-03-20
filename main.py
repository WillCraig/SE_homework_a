from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

WEBSITE = "https://www.shino.de/parkcalc/"


def test_date_error():
    browser = webdriver.Chrome()
    try:
        browser.get(WEBSITE)

        assert "Parking Cost Calculator" in browser.title

        ending_date = browser.find_element(By.NAME, 'LeavingDate')
        ending_date.clear()
        ending_date.send_keys("nope")
        ending_date.send_keys(Keys.RETURN)

        sleep(1)

        calculate_button = browser.find_element(By.NAME, 'Submit')

        sleep(1)
        calculate_button.click()

        # wait for the search to complete.
        sleep(1)

        # This will indicate an error with the date format.
        assert "ERROR! Enter A Correctly Formatted Date" in browser.page_source

    finally:
        browser.close()


def correct_use():
    browser = webdriver.Chrome()
    try:
        browser.get(WEBSITE)

        assert "Parking Cost Calculator" in browser.title

        starting_date = browser.find_element(By.NAME, 'StartingDate')
        starting_date.clear()
        starting_date.send_keys("07/25/1999")
        starting_date.send_keys(Keys.RETURN)

        ending_date = browser.find_element(By.NAME, 'LeavingDate')
        ending_date.clear()
        ending_date.send_keys("07/25/2023")
        ending_date.send_keys(Keys.RETURN)

        # StartingTime
        start_time = browser.find_element(By.NAME, 'StartingTime')
        start_time.clear()
        start_time.send_keys("07:00")
        start_time.send_keys(Keys.RETURN)

        sleep(1)

        calculate_button = browser.find_element(By.NAME, 'Submit')

        sleep(1)
        calculate_button.click()

        # wait for the search to complete.
        sleep(1)

        # label = browser.find_element(By.CLASS_NAME, "SubHead")
        content = browser.page_source

        # This will indicate an error with the date format.
        assert "$ 157,788.00" in content
        assert "(8765 Days, 17 Hours, 0 Minutes)" in content

    finally:
        browser.close()


if __name__ == '__main__':
    print(f"Parking test...({WEBSITE})..\n")

    test_date_error()

    correct_use()

    print("\n\nEND OF PROGRAM..")
