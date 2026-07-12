from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    field_delay = wait.until(EC.presence_of_element_located(
       (By.CSS_SELECTOR, "#delay")
    ))

    field_delay.clear()
    field_delay.send_keys("45")

    button_8 = driver.find_element(
        By.XPATH, "//*[contains(@class, 'btn') and contains(., '8')]"
    )
    button_8.click()

    button_sum = driver.find_element(
        By.XPATH, "//*[contains(@class, 'btn') and contains(., '+')]"
    )
    button_sum.click()

    button_7 = driver.find_element(
        By.XPATH, "//*[contains(@class, 'btn') and contains(., '7')]"
    )
    button_7.click()

    button_res = driver.find_element(
        By.XPATH, "//*[contains(@class, 'btn') and contains(., '=')]"
    )
    button_res.click()

    result = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"

    driver.quit()
