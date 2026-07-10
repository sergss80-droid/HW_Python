from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    driver.maximize_window()
    sleep(1)
    click_button = driver.find_element(
        By.CSS_SELECTOR, 'a[href="/forms/post"]')
    click_button.click()
    sleep(2)

    assert "/forms/post" in driver.current_url
    driver.back()
    sleep(3)
    assert driver.current_url == "https://httpbin.org/"

    driver.quit()
