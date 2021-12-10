from selenium import webdriver
import time
import sys
import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import pytest
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# for select value from dropdown 
from selenium.webdriver.support.ui import Select

#for screenshot
from PIL import Image
from Screenshot import Screenshot_Clipping

driver=webdriver.Chrome()

driver.get("http://www.tutorialsninja.com/demo/")
driver.maximize_window()

#search mobile 
driver.find_element(By.NAME,"search").click()
driver.find_element(By.NAME,"search").send_keys("Palm Treo Pro")
driver.find_element(By.NAME,"search").send_keys(Keys.ENTER)

#click on particular mobile
mobile_locator=By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/a/img"
mobile=driver.find_element(*mobile_locator).click()

#screenshot 
driver.save_screenshot("ss.png")
time.sleep(3)
screenshot = Image.open("ss.png")
screenshot.show()

#add to cart
add_to_cart=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/input[1]"
cart=driver.find_element(*add_to_cart)
cart.send_keys(Keys.BACKSPACE)
time.sleep(3)
cart.send_keys("2")
time.sleep(3)

#for scrolldown one step
driver.execute_script("window.scrollTo(0,300);")
time.sleep(2)

submit=By.XPATH,"/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div/button"
driver.find_element(*submit).click()

homepage_loactor=By.XPATH,"/html/body/header/div/div/div[1]/div/h1/a"
homepage=driver.find_element(*homepage_loactor).click()

driver.find_element(By.NAME,"search").click()
driver.find_element(By.NAME,"search").send_keys("HP LP3065")
driver.find_element(By.NAME,"search").send_keys(Keys.ENTER)

#for scrolldown two step
driver.execute_script("window.scrollTo(300,600);")
time.sleep(2)

laptop_loactor=By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/a/img"
laptop=driver.find_element(*laptop_loactor).click()
time.sleep(2)

#for scrolldown one step
driver.execute_script("window.scrollTo(0,300);")
time.sleep(2)

#date
date_loactor=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div/input"
date=driver.find_element(*date_loactor)
date.send_keys(10*Keys.BACKSPACE)
time.sleep(2)
date.send_keys("2022-12-31")
time.sleep(2)

#cart submit
cart_submit=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/button"
cart=driver.find_element(*cart_submit).click()
time.sleep(2)

#cart item nevbar
cart_item=By.XPATH,"/html/body/header/div/div/div[3]/div/button"
cart_i=driver.find_element(*cart_item).click()
time.sleep(2)

#chekout navbar
checkout_loactor=By.XPATH,"/html/body/header/div/div/div[3]/div/ul/li[2]/div/p/a[2]/strong"
checkout=driver.find_element(*checkout_loactor).click()
time.sleep(2)


#create guest account
guest_checkout=By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]/label/input"
guest=driver.find_element(*guest_checkout).click()
time.sleep(2)

#continue
conti=By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/input"
driver.find_element(*conti).click()
time.sleep(2)

#one step scroll down
driver.execute_script("window.scrollTo(0,300);")
time.sleep(2)

# Customer details form
#first name
fname_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/fieldset/div[2]/input"
fname=driver.find_element(*fname_locator)
fname.send_keys("Jignesh")
time.sleep(2)


#lname
lname_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/fieldset/div[3]/input"
lname=driver.find_element(*lname_locator)
lname.send_keys("Patel")
time.sleep(2)


#email
email_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/fieldset/div[4]/input"
email=driver.find_element(*email_locator)
email.send_keys("jignesh@gmail.com")
time.sleep(2)

#Telephone
telephone_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/fieldset/div[5]/input"
telephone=driver.find_element(*telephone_locator)
telephone.send_keys("9896989898")
time.sleep(2)


#company
company_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/fieldset/div[1]/input"
company=driver.find_element(*company_locator)
company.send_keys("NIXI")
time.sleep(2)

#Address 1
add1_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/fieldset/div[2]/input"
add1=driver.find_element(*add1_locator)
add1.send_keys("4th floor,GNFC DATACENTRE")
time.sleep(2)


#Address 2
add2_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/fieldset/div[3]/input"
add2=driver.find_element(*add2_locator)
add2.send_keys("S.G.Highway")
time.sleep(2)

#city
city_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/fieldset/div[4]/input"
city=driver.find_element(*city_locator)
city.send_keys("Ahmedabad")
time.sleep(2)

#postcode
pin_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/fieldset/div[5]/input"
pin=driver.find_element(*pin_locator)
pin.send_keys("380054")
time.sleep(4)


#county
select = Select(driver.find_element_by_id('input-payment-country'))
select.select_by_visible_text('India')
select.select_by_value('99')

#for scrolldown two step
driver.execute_script("window.scrollTo(300,600);")
time.sleep(3)

#State
state_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/fieldset/div[7]/select"
state=driver.find_element(*state_locator)
state.send_keys("Gujarat")
time.sleep(4)

#continue
contin_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/input"
contin=driver.find_element(*contin_locator).click()
time.sleep(3)


#add comment
ad_comment=By.XPATH,"/html/body/div[2]/div/div/div/div[4]/div[2]/div/p[4]/textarea"
comment=driver.find_element(*ad_comment)
comment.send_keys("Home delivery")
time.sleep(3)

con_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[4]/div[2]/div/div[2]/div/input"
con=driver.find_element(*con_locator).click()
time.sleep(2)

#terms  and condition
term=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[5]/div[2]/div/div[2]/div/input[1]")
term.click()

#final submit 
subm_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[5]/div[2]/div/div[2]/div/input[2]"
subm=driver.find_element(*subm_locator).click()
time.sleep(3)

#total amount
total_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[6]/div[2]/div/div[1]/table/tfoot/tr[3]/td[2]"
total=driver.find_element(*total_locator)
print("Total bill",total.text)
time.sleep(3)

#confirm order
co_locator=By.XPATH,"/html/body/div[2]/div/div/div/div[6]/div[2]/div/div[2]/div/input"
co=driver.find_element(*co_locator).click()
time.sleep(3)

#confirmation massage
confirm_msg= By.CSS_SELECTOR,"#content > h1"
#confirm_msg=By.XPATH,"/html/body/div[2]/div/div/p[1]"
message=driver.find_element(*confirm_msg)
print(message.text)
time.sleep(3)

