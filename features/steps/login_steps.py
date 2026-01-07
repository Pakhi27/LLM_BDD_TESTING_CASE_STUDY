from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

@given('user is on login page')
def step_open_login(context):
    options = Options()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)

@when('user enters valid username and password')
def step_enter_credentials(context):
    context.driver.find_element(By.ID, "username").send_keys("tomsmith")
    context.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

@when('clicks login button')
def step_click_login(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

@then('user should be redirected to dashboard')
def step_verify_dashboard(context):
    assert "/secure" in context.driver.current_url
    context.driver.quit()
