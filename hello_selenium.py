from selenium import webdriver

# Path to the Chrome driver executable
# chrome_driver_path = "/path/to/chromedriver"
# Create a new instance of the Chrome driver
# Navigate to the URL of the webpage you want to visit
# Find the search box element on the page
# search_box = driver.find_element(by="name",value="q")
# Type a search query into the search box
# search_box.send_keys("Python Selenium")
# Submit the search query
# search_box.submit()
# Wait for the search results to load
# driver.implicitly_wait(700)
# Close the browser window
# driver.quit()

driver = webdriver.Chrome()
driver.get("https://testdev.scxinglin.com/plat/index/login")
CLS="class name"
elements = driver.find_elements(CLS, "el-input__inner")
# print(len(elements))
elements[0].send_keys('604133')
elements[1].send_keys('111111')
tag="tag name"

button = driver.find_element(CLS,'el-row').find_element(tag,"button")
print("button -> ",button.text)
button.click()

print(driver.title)

driver.implicitly_wait(30)

driver.quit()
