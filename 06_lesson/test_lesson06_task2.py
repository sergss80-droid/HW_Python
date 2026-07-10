from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
       "name": "SESSION",
       "value": "NDEyYzE3NDQtMmFmMi00NGZiLTk5YmQtOTg3NDIxNWI5ZGRk",
       "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/test_python_lesson1")
    url_1 = driver.execute_script("return window.location.href;")
    print(f"URL первого пользователя: {url_1}")

    driver.delete_all_cookies()
    driver.refresh()

    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "MTZhZjI3MGItN2FkZS00ZjEyLWJlMGItYWJlYWZlNmE0NGZh",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/test_python_lesson2")
    url_2 = driver.execute_script("return window.location.href;")
    print(f"URL второго пользователя: {url_2}")

    assert url_1 != url_2, (
        f"Ошибка: URL пользователей совпадают!\n"
        f"user 1: {url_1}\n"
        f"user 2: {url_2}"
    )

    driver.quit()
