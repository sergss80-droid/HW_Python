from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ajax_content():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_btn = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_btn.click()

    hello_text = wait.until(
        EC.visibility_of_element_located(
         (By.XPATH, "//h4[text()='Hello World!']"))
    )
    assert hello_text.is_displayed(), (
        "Элемент с текстом 'Hello World!' не отображается"
    )
    assert hello_text.text == "Hello World!",  (
        f"Текст элемента не 'Hello World!', а '{hello_text.text}'"
    )

    driver.save_screenshot("screenshots/full_screen.png")

    hello_text = wait.until(
        EC.visibility_of_element_located(
         (By.XPATH, "//h4[text()='Hello World!']"))
    )
    assert hello_text.is_displayed(), (
        "Элемент с текстом 'Hello World!' не отображается"
    )
    assert hello_text.text == "Hello World!", (
        f"Текст элемента не 'Hello World!', а '{hello_text.text}'"
    )

    driver.quit()
