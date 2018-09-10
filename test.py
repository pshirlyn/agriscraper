#! usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options


#open browser
browser = webdriver.Firefox()

#check that website opened properly
browser.get('http://agmarknet.gov.in/PriceAndArrivals/CommodityWiseDailyReport.aspx')
assert "Agriculture" in browser.title

for i in range(1, 32):
	#sets year and month
	year = Select(browser.find_element_by_name('ctl00$cphBody$drpDwnYear'))
	year.select_by_visible_text("2011")

	month = Select(browser.find_element_by_name('ctl00$cphBody$drpDwnMonth'))
	month.select_by_visible_text("January")

	wait = WebDriverWait(browser, 10)


	#time.sleep(10) #Hopefully date loads by this time
	wait.until(EC.text_to_be_present_in_element((By.XPATH, '//table[@id="cphBody_Calendar1"]/tbody/tr[1]/td/table/tbody/tr/td'), "January 2011"))

	date = browser.find_element_by_link_text(str(i))
	date.click()


	submit = wait.until(EC.presence_of_element_located((By.ID, "cphBody_Submit_list")))
	submit.click()

	#on the groundnut selection page
	item = wait.until(EC.presence_of_element_located((By.ID, "cphBody_GridView1_RowLevelCheckBox_36")))
	item.click()

	item_submit = wait.until(EC.presence_of_element_located((By.ID, "cphBody_btnSubmit")))
	item_submit.click()


	#excel page
	excel_dl = wait.until(EC.presence_of_element_located((By.ID, "cphBody_Button1")))
	#print("tested download for "+str(i))

	excel_dl.click()


	#back to start page
	browser.back()
	browser.back()


	

