from selenium import webdriver

browser=webdriver.Chrome("chromedriver.exe")
browser.get('https://www.narendramodi.in/category/text-speeches')


links=browser.find_element_by_css_selector('.left_class a').get_attribute('href')

print(links)