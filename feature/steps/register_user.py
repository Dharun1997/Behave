import time

from selenium import webdriver
from behave import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@given(u'Launch Chrome Browser')
def step_impl(context):
    context.service_obj = Service("C:\Driver\chromedriver_win32\chromedriver.exe")
    context.driver = webdriver.Chrome(service=context.service_obj)

@when(u'Login Page will be opened')
def step_impl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")

@then(u'Dashboard page will be shown')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@given('Click on the Customers tab at the left side and select Customers option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p").click()
    context.driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']/p").click()

@when(u'Click on Add New option button')
def step_impl(context):
    context.driver.find_element(By.XPATH, " // a[ @ href = '/Admin/Customer/Create'] / i").click()

@when('Enter mail "{mail}" firstname "{firstname}" lastname "{lastname}" dob "{dob}" in the corresponding fields')
def step_impl(context, mail, firstname, lastname, dob):
    context.driver.find_element(By.XPATH,"//input[@id='Email']").send_keys(mail)
    context.driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(firstname)
    context.driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys(lastname)
    context.driver.find_element(By.XPATH, "//input[@name='DateOfBirth']").send_keys(dob)
    time.sleep(3)


@when(u'Click on Save button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "// button[ @ name = 'save']").click()
    time.sleep(3)

@then(u'User must be successfully registered')
def step_impl(context):
    button = context.driver.find_element(By.XPATH, " // html / body / div[3] / div[1] / div[1]")
    if button.is_displayed():
        assert True,"Test case passed"
    else:
        assert False,"Test case failed"














