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

for i in range(11, 32):
	#refresh page each time you get to beginning
	browser.refresh()

	#sets year and month
	year = Select(browser.find_element_by_name('ctl00$cphBody$drpDwnYear'))
	year.select_by_visible_text("2011")

	month = Select(browser.find_element_by_name('ctl00$cphBody$drpDwnMonth'))
	month.select_by_visible_text("January")

	#wait until the table loads the correct month and year
	wait = WebDriverWait(browser, 20)
	#time.sleep(12)


	wait.until(EC.text_to_be_present_in_element((By.XPATH, '//table[@id="cphBody_Calendar1"]/tbody/tr[1]/td/table/tbody/tr/td'), "January 2011"))

	date = browser.find_element_by_link_text(str(i))
	date.click()

	#submit button id cphBody_Submit_list
	#submit = wait.until(EC.presence_of_element_located((By.ID, "cphBody_GridView1_RowLevelCheckBox1_34")))
	submit = wait.until(EC.presence_of_element_located((By.ID, "cphBody_Submit_list")))
	submit.click()

	#on the groundnut selection page
	time.sleep(8) #allow user to manually click
	#item = wait.until(EC.presence_of_element_located((By.ID, "//td[normalize-space() = 'Groundnut']")))
	#item = wait.until(EC.presence_of_element_located((By.XPATH, ".//*[contains(text(), 'Groundnut')]")))
	#item.click()

	item_submit = wait.until(EC.presence_of_element_located((By.ID, "cphBody_btnSubmit")))
	item_submit.click()


	#excel page
	excel_dl = wait.until(EC.presence_of_element_located((By.ID, "cphBody_Button1")))
	#print("tested download for "+str(i))

	excel_dl.click()


	#back to start page
	browser.back()
	browser.back()


	

