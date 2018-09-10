#! usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#open browser
browser = webdriver.Firefox()
FirefoxProfile fxProfile = new FirefoxProfile();

fxProfile.setPreference("browser.download.folderList",2);
fxProfile.setPreference("browser.download.manager.showWhenStarting",false);
fxProfile.setPreference("browser.download.dir","/home/pshirlyn/Documents/Programming/urop");
fxProfile.setPreference("browser.helperApps.neverAsk.saveToDisk","text/csv");


#check that website opened properly
browser.get('http://agmarknet.gov.in/PriceAndArrivals/CommodityWiseDailyReport.aspx')
assert "Agriculture" in browser.title

#sets year and month
year = Select(browser.find_element_by_name('ctl00$cphBody$drpDwnYear'))
year.select_by_visible_text("2011")

month = Select(browser.find_element_by_name('ctl00$cphBody$drpDwnMonth'))
month.select_by_visible_text("January")

for i in range(1, 32):
	date = browser.find_element_by_link_text('1')
	date.click()

	wait = WebDriverWait(browser, 10)
	submit = wait.until(EC.presence_of_element_located((By.ID, "cphBody_Submit_list")))
	submit.click()

	#on the groundnut selection page
	item = wait.until(EC.presence_of_element_located((By.ID, "cphBody_GridView1_RowLevelCheckBox_36")))
	item.click()

	item_submit = wait.until(EC.presence_of_element_located((By.ID, "cphBody_btnSubmit")))
	item_submit.click()


	#excel page
	excel_dl = wait.until(EC.presence_of_element_located((By.ID, "cphBody_Button1")))
	print("tested download for "+str(i))



	#back to start page
	browser.back()
	browser.back()


	#excel_dl.click()

