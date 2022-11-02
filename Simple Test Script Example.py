from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()

driver.implicitly_wait(3)

# Google logo verify:
driver.find_element(By.XPATH, '//img[@class="lnXdpd"]')
print("Logo is found")

# Google tittle verify:
assert "Google" in driver.title
print("Title is OK:", driver.title)

# Google URL verify:
assert "https://www.google.com/" in driver.current_url
print("URL is OK:", driver.current_url)

wait = WebDriverWait(driver, 3)
wait.until(EC.element_to_be_clickable((By.NAME, "q")))  # before By (( , not (

#  Find Search bar and sent keys there:
elem = driver.find_element(By.NAME, "q")
elem.click()
elem.send_keys("ABC")
elem.click()

# way 1, hit "Enter" on the Keyboard after keys sending:
# elem.send_keys(Keys.RETURN)  # Keys - K is large + library special for Keys, not keys!

# Find element value, then store this value to variable "btnk"
btnk = driver.find_element(By.NAME, "btnK").get_attribute("value")

# Assert (compare) stored element value with required value
assert btnk == "Google Search"

# Same element verification for "Google Search" button
if btnk is not None:
    print("Google Search button is OK")
else:
    print("NO Google Search button")


# way2, hit Search by button "Search" on the bottom of page after keys sending:
driver.find_element(By.NAME, "btnK").click()
# driver.find_element(By.NAME, "btnK").submit()

driver.find_element(By.XPATH, "//h3[contains(.,'ABC Home Page - ABC.com')]").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click() # OR By Partial link text which we took from
# inspect: > ABC Home Page - ABC.com < "

assert "ABC Home Page - ABC.com" in driver.title
print("Title is OK:", driver.title)
if "ABC Home Page - ABC.com" not in driver.title:
    raise Exception("Title for ABC page is wrong!")  # raise exception to stop code if Title is incorrect

assert "https://abc.com/" in driver.current_url
print("New opened page URL is correct:", driver.current_url)

# wait max 5 sec for page loading, then show "Load Error"
driver.set_page_load_timeout(5)
driver.find_element(By.LINK_TEXT, "Browse").click()
# driver.find_element(By.XPATH, "(//span[contains(.,'browse')])[1]").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Jimmy Kimmel Live!")
print("Show was found")
driver.get("https://abc.com/shows/jimmy-kimmel-live")
time.sleep(1)
assert"Watch Jimmy Kimmel Live! TV Show - ABC.com" in driver.title
print("Title is OK:", driver.title)


jimmyShowURL = "https://abc.com/shows/jimmy-kimmel-live"
assert jimmyShowURL == driver.current_url
if jimmyShowURL != driver.current_url:
    print("Current Jimmy Kimmel Show URL is different and it is: ", driver.current_url)
else:
    print("Current Dance Show URL is OK: ", driver.current_url)


# Find element value
jimmyPageLogo = driver.find_element(By.XPATH, '//*[@title="Jimmy Kimmel Live!"]').get_attribute("title")
# jimmyPageLogo = driver.find_element(By.XPATH, '//img[@title="Jimmy Kimmel Live!"]')
assert jimmyPageLogo == "Jimmy Kimmel Live!"
assert jimmyPageLogo in driver.page_source
print("Page Logo was found")

try:
    driver.find_element(By.PARTIAL_LINK_TEXT, "VIEW SCHEDULE").click()
    print("Jimmy Kimmel Show Schedule is available")
except NoSuchElementException:
    print("Jimmy Kimmel Show Schedule is not available")

# time.sleep(1)
if driver.find_element(By.PARTIAL_LINK_TEXT, "Jimmy Kimmel Live Schedule for the Week of").is_displayed():
    print("Schedule is displayed")
else:
    print("Schedule is not displayed")

driver.quit()
