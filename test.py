#! usr/bin/env python3
#import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Firefox()

#driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')


browser.get('http://agmarknet.gov.in/PriceAndArrivals/CommodityWiseDailyReport.aspx')
assert "Agriculture" in browser.title


year = Select(browser.find_element_by_name('ctl00$cphBody$drpDwnYear'))
year.select_by_visible_text("2011")
#year = browser.find_element_by_xpath("//select[@name='ctl00$cphBody$drpDwnYear']")

#month = browser.find_element_by_class_name("ctl00$cphBody$drpDwnMonth")
month = Select(browser.find_element_by_name('ctl00$cphBody$drpDwnMonth'))
month.select_by_visible_text("January")

#date = brower.find_element_by_xpath("//table[@id='cphBody_Calendar1']/tr[3]/td[@align='center']")
date = browser.find_element_by_link_text('1')
date.click()

wait = WebDriverWait(browser, 10)
submit = wait.until(EC.presence_of_element_located((By.ID, "cphBody_Submit_list")))
submit.click()

#on the groundnut selection page
browser.findElement(By.id("idOfTheElement")).click();


#class DataSpider(scrapy.Spider):
