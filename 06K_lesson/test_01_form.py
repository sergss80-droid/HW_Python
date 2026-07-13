from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_forms():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    input_first_name = wait.until(EC.presence_of_element_located(
       (By.NAME, "first-name")
    ))
    input_first_name.send_keys("Иван")

    input_last_name = driver.find_element(By.NAME, "last-name")
    input_last_name.send_keys("Петров")

    input_last_name = driver.find_element(By.NAME, "address")
    input_last_name.send_keys("Ленина, 55-3")

    input_last_name = driver.find_element(By.NAME, "e-mail")
    input_last_name.send_keys("test@skypro.com")

    input_last_name = driver.find_element(By.NAME, "phone")
    input_last_name.send_keys("+7985899998787")

    input_last_name = driver.find_element(By.NAME, "city")
    input_last_name.send_keys("Москва")

    input_last_name = driver.find_element(By.NAME, "country")
    input_last_name.send_keys("Россия")

    input_last_name = driver.find_element(By.NAME, "job-position")
    input_last_name.send_keys("QA")

    input_last_name = driver.find_element(By.NAME, "company")
    input_last_name.send_keys("SkyPro")

    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    field_zip_code = driver.find_element(By.ID, "zip-code")
    color_zip_code = field_zip_code.value_of_css_property('border-color')
    assert color_zip_code == "rgb(245, 194, 199)" in color_zip_code

    fields = ["first-name",
              "last-name",
              "address",
              "city",
              "country",
              "e-mail",
              "phone",
              "job-position",
              "company"]

    for field_id in fields:
        field_element = wait.until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        border_color = field_element.value_of_css_property("border-color")
        assert border_color == "rgb(186, 219, 204)", (
             f"Поле {field_id} не подсвечено зеленым"
        )

    driver.quit()
