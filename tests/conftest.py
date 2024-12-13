import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
from dotenv import load_dotenv




# Load environment variables from .env file
load_dotenv()

@pytest.fixture(scope='function')
def driver(request):
    username = "pushpa_sathish"
    access_key = "cgubzyOubHatV66TTQyFMyWI2HJZ95psh5HzKiUXYkyFs6Xhmc"
    #selenium_endpoint = f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub"

    selenium_endpoint = f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub"

    options = webdriver.ChromeOptions()
    lt_options = {
        "platform": "Windows 10",
        "browserName": "Chrome",
        "version": "latest",
        "build": "LambdaTest Sample Build",
        "name": request.node.name,
        "video": True,
        "visual": True,
        "network": True,
        "console": True,
    }
    options.set_capability("LT:Options", lt_options)

    driver = webdriver.Remote(command_executor=selenium_endpoint, options=options)
    yield driver
    driver.quit()
