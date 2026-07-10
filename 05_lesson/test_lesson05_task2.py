from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    sleep(1)

    old_url = driver.current_url

    driver.find_element(By.CSS_SELECTOR, '[name="custname"]').send_keys(
        "Serg"
    )
    sleep(2)
    driver.find_element(
        By.TAG_NAME, "button").click()
    sleep(2)

    assert driver.current_url != old_url

    driver.quit()
