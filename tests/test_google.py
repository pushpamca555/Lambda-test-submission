from datetime import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_drog_and_drop(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

@pytest.mark.smoke
def test_title(driver):
        driver.get(r'https://www.lambdatest.com/selenium-playground/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//a[contains(text(),'Simple Form Demo')]").click()
        title = driver.current_url
        assert "simple-form-demo" in title, "tetx is not present n the URL"
        val = "Welcome to LambdaTest"
        driver.find_element(By.ID, "user-message").send_keys(val)
        # driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys(val)
        driver.find_element(By.ID, "showInput").click()
        text = driver.find_element(By.CSS_SELECTOR, '#message').text
        assert text == val

@pytest.mark.smoke
def test_item(driver):
        driver.get('https://www.lambdatest.com/selenium-playground/')
        driver.find_element(By.XPATH, "//a[contains(text(),'Drag & Drop Sliders')]").click()
        time.sleep(20)
        ActionChains(driver).move_by_offset(946, 349).pause(2).click().perform()
        exp_val = '95'
        obtained_val = driver.find_element(By.ID, "rangeSuccess").text
        assert exp_val, obtained_val == "Value is not equal to 95"
