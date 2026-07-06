from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    all_links = driver.find_elements(By.TAG_NAME, "a")

    assert len(all_links) == 9

    for index, link in enumerate(all_links, start=1):
        assert link.is_displayed()

    driver.quit()
