from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    options = Options()
    driver = webdriver.Firefox(options=options)

    try:
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get(
            "https://www.saucedemo.com"
        )

        input_username = wait.until(EC.presence_of_element_located(
           (By.ID, "user-name")
        ))
        input_username.send_keys("standard_user")

        input_password = driver.find_element(By.ID, "password")
        input_password.send_keys("secret_sauce")

        button_login = driver.find_element(By.ID, "login-button")
        button_login.click()

        add_backpack = wait.until(EC.presence_of_element_located(
           (By.ID, "add-to-cart-sauce-labs-backpack")
        ))
        add_backpack.click()

        add_bolt_t_Shirt = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        add_bolt_t_Shirt.click()

        add_onesie = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        )
        add_onesie.click()

        button_cart_link = driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        )
        button_cart_link.click()

        button_checkout = driver.find_element(By.ID, "checkout")
        button_checkout.click()

        input_first_name = wait.until(EC.presence_of_element_located(
           (By.ID, "first-name")
        ))
        input_first_name.send_keys("Сергей")

        input_last_name = driver.find_element(By.ID, "last-name")
        input_last_name.send_keys("Саватнеев")

        input_zip_code = driver.find_element(By.ID, "postal-code")
        input_zip_code.send_keys("452005")

        button_continue = driver.find_element(By.ID, "continue")
        button_continue.click()

        total_element = wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"
            ))
            )
        total_text = total_element.text
        print(f"Получена итоговая стоимость: {total_text}")
        # 9. Проверяем, что итоговая сумма равна $58.29.
        expected_total = "Total: $58.29"
        assert total_text == expected_total, (
            f"Ошибка! Итоговая сумма не совпадает. "
            F"Ожидалось: {expected_total}, Получено: {total_text}"
        )
        print("Проверка пройдена: итоговая сумма = $58.29")

    except AssertionError as e:
        print(f"\n Ошибка проверки {e}")
        raise

    finally:
        driver.quit()
