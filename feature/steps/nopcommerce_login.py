from selenium import webdriver
from behave import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@given('I launch Chrome browser')
def step_impl(context):
    context.service_obj=Service("C:\Driver\chromedriver_win32\chromedriver.exe")
    context.driver=webdriver.Chrome(service=context.service_obj)

@when('I open Nopcommerce login page')
def step_impl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")

@when('Enter email "{email}" and password "{password}"')
def step_impl(context, email, password):
    context.driver.find_element(By.XPATH,"//*[@id='Email']").clear()
    context.driver.find_element(By.XPATH, "//*[@id='Email']").send_keys(email)
    context.driver.find_element(By.XPATH, "//*[@id='Password']").clear()
    context.driver.find_element(By.XPATH, "//*[@id='Password']").send_keys(password)

@when('Click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then('Login must be successful')
def step_impl(context):
    context.title=context.driver.find_element(By.XPATH,"//h1[contains(text(),'Dashboard')]").text
    if context.title=="Dashboard":
        assert True
        context.driver.close()













