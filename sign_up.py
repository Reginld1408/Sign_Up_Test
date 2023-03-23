import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PageObjectModelOne.Pages.search_page import SearchPageProp


def test_sample():
    serv_obj = Service("C:/Users/sirwi/Downloads/chromedriver_win32/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=serv_obj, options=options)
    driver.implicitly_wait(10)

    driver.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser")

    # sign up
    search_page = SearchPageProp()

    # first name
    first_name = driver.find_element(By.XPATH, "//input[@id='FirstName']")
    first_name.click()
    first_name.send_keys("Jeremy")

    # surname
    surname = driver.find_element(By.XPATH, "//input[@id='Surname']")
    surname.click()
    surname.send_keys("McGowan")

    # e-post
    e_post = driver.find_element(By.XPATH, "//input[@id='E_post']")
    e_post.click()
    e_post.send_keys("9999")

    # mobile number
    mobile_num = driver.find_element(By.XPATH, "//input[@id='Mobile']")
    mobile_num.click()
    mobile_num.send_keys("9053360041")

    # username
    user_name = driver.find_element(By.XPATH, "//input[@id='Username']")
    user_name.click()
    user_name.send_keys("JGowan")

    # password
    password = driver.find_element(By.XPATH, "//input[@id='Password']")
    password.click()
    password.send_keys("Lk4V56$128")

    # confirm password
    confirm_pass = driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']")
    confirm_pass.click()
    confirm_pass.send_keys("Lk4V56$128")

    # click submit button
    submit_btn = driver.find_element(By.XPATH, "//input[@id='submit']")
    submit_btn.click()
    print("User 'JGowan' Successfully Created")

    # test login after sign up
    login_page = driver.find_element(By.XPATH, "//*[@id='navbarColor01']/form/ul/li[2]/a")
    login_page.click()

    # username login
    user_name_login = driver.find_element(By.XPATH, "//*[@id='Username']")
    user_name_login.click()
    user_name_login.send_keys("JGowan")

    # password login
    password_login = driver.find_element(By.CSS_SELECTOR, "#Password")
    password_login.click()
    password_login.send_keys("Lk4V56$128")

    # click login button
    login_btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]")
    login_btn.click()
    print("Login Successful")

    # take screenshot of successful login
    driver.save_screenshot('screenshot#' + str(random.randint(1, 101)) + '.png')
    time.sleep(1)

    # create new customer
    new_customer_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Create New']")
    new_customer_btn.click()

    # customer name
    customer_name = driver.find_element(By.XPATH, "//input[@id='Name']")
    customer_name.click()
    customer_name.send_keys("Jeremy")

    # company name
    company_name = driver.find_element(By.XPATH, "//input[@id='Company']")
    company_name.click()
    company_name.send_keys("McGowan Phone Repair")

    # company address
    company_address = driver.find_element(By.XPATH, "//input[@id='Address']")
    company_address.click()
    company_address.send_keys("103 Elm Lane")

    # company city
    company_city = driver.find_element(By.XPATH, "//input[@id='City']")
    company_city.click()
    company_city.send_keys("Ontario")

    # company phone
    company_phone = driver.find_element(By.XPATH, "//input[@id='Phone']")
    company_phone.click()
    company_phone.send_keys("9058872344")

    # company email
    company_email = driver.find_element(By.XPATH, "//input[@id='Email']")
    company_email.click()
    company_email.send_keys("McGowanRepair@domain")

    # click create new customer button
    create_customer_btn = driver.find_element(By.XPATH, "//input[@value='Create']")
    create_customer_btn.click()
    print("Customer 'Jeremy' Created")

    # search for created customer, edit, confirm change, delete, confirm deleted customer
    driver.find_element(By.ID, search_page.customer_search_field_id).click()
    driver.find_element(By.ID, search_page.customer_search_field_id).send_keys("Jeremy")
    driver.find_element(By.XPATH, search_page.customer_search_btn_xpath).click()

    # take screenshot of new customer details
    driver.save_screenshot('screenshot#' + str(random.randint(1, 101)) + '.png')
    time.sleep(1)

    # edit new customer
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/table/tbody/tr[2]/td[7]/a[1]").click()

    # update name
    update_customer_name = driver.find_element(By.XPATH, "//*[@id='Name']")
    update_customer_name.click()
    update_customer_name.clear()
    time.sleep(2)
    update_customer_name.send_keys("Davis")
    save_btn = driver.find_element(By.XPATH, "/html/body/div/form/div/div[7]/div/input")
    save_btn.click()
    time.sleep(2)
    print("Customer edit name changed to 'Davis' ")

    # search for previous and new edited customer
    driver.find_element(By.ID, search_page.customer_search_field_id).click()
    driver.find_element(By.ID, search_page.customer_search_field_id).send_keys("Jeremy")
    driver.find_element(By.XPATH, search_page.customer_search_btn_xpath).click()
    time.sleep(2)
    driver.find_element(By.ID, search_page.customer_search_field_id).clear()
    driver.find_element(By.ID, search_page.customer_search_field_id).send_keys("Davis")
    driver.find_element(By.XPATH, search_page.customer_search_btn_xpath).click()
    time.sleep(2)

    # take screenshot of updated customer name
    driver.save_screenshot('screenshot#' + str(random.randint(1, 101)) + '.png')
    time.sleep(1)

    # delete new customer
    driver.find_element(By.XPATH, "/html/body/div/div/table/tbody/tr[2]/td[7]/a[3]").click()

    # confirm delete new customer
    driver.find_element(By.XPATH, "/html/body/div/div/form/div/input").click()
    time.sleep(1)

    # recheck customer search to confirm deleted
    driver.find_element(By.ID, search_page.customer_search_field_id).click()
    driver.find_element(By.ID, search_page.customer_search_field_id).send_keys("Davis")
    driver.find_element(By.XPATH, search_page.customer_search_btn_xpath).click()
    print("Customer 'Davis' Deleted")
    time.sleep(2)

    # take screenshot confirming deleted customer - no match
    driver.save_screenshot('screenshot#' + str(random.randint(1, 101)) + '.png')
    time.sleep(1)

    # close driver
    driver.close()


test_sample()
