import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE

# Main URL:
url = "https://www.nasa.gov/"

# Main Title:
title_main_page = "NASA"


# Set up random delay:


def delay_1_2():
    time.sleep(random.randint(1, 3))


# Icons XPATH:

twitter = '//img[@alt="Twitter"]'
facebook = '//img[@alt="Facebook"]'
instagram = '//img[@alt="Instagram"]'
snapchat = '//img[@alt="snapchat"]'
youtube = '//img[@alt="YouTube"]'
tumblr = '//img[@alt="Tumblr"]'
# pinterest = '//img[@alt="Pinterest"]'
pinterest = "//img[@src='/sites/default/files/styles/full_width/public/thumbnails/image/pinterest-64px.png?itok" \
            "=6xhSmVFc'] "
linkedin = '//img[@alt="LinkedIn"]'
giphy = '//img[@alt="GIPHY"]'
flickr = '//img [@alt="Flickr"]'
twitch = '//img[@alt="Twitch"]'
soundcloud = '//img[@alt="Soundcloud"]'
reddit = '//img[@alt="Reddit"]'
dailymotion = '//img[@alt="Daily Motion"]'

# Social media URLs from documentation:
Twitter_URL = "https://twitter.com/nasa"
Facebook_URL = "https://www.facebook.com/NASA/"
Instagram_URL = "https://www.instagram.com/nasa/"
Snapchat_URL = "https://snapchat.com/add/nasa"
YouTube_URL = "https://www.youtube.com/NASA"
Tumblr_URL = "https://nasa.tumblr.com/"
Pinterest_URL = "https://www.pinterest.com/nasa/"
GIPHY_URL = "https://giphy.com/nasa"
LinkedIn_URL = "https://www.linkedin.com/company/nasa/"
Flickr_URL = "https://www.flickr.com/photos/nasahqphoto/"
Twitch_URL = "https://www.twitch.tv/nasa/"
SoundCloud_URL = "https://soundcloud.com/nasa"
Reddit_URL = "https://www.reddit.com/user/nasa"
Dailymotion_URL = "https://www.dailymotion.com/NASA"

# Social media Titles from documentation:
Twitter_Title = " Twitter"
Facebook_Title = "NASA - National Aeronautics and Space Administration | Government Organization | Facebook"
Instagram_Title = "NASA (@nasa) • Instagram photos and videos"
Snapchat_Title = "NASA (@nasa) on Snapchat"
YouTube_Title = "NASA - YouTube"
Tumblr_Title = "NASA"
Pinterest_Title = "NASA (nasa) - Profile | Pinterest"
GIPHY_Title = "NASA GIFs - Find & Share on GIPHY"
LinkedIn_Title = "Sign In | LinkedIn"
Flickr_Title = "NASA HQ PHOTO | Flickr"
Twitch_Title = "NASA - Twitch"
SoundCloud_Title = "Stream NASA | Listen to podcast episodes online for free on SoundCloud"
Reddit_Title = "NASA (u/nasa) - Reddit"
Dailymotion_Title = "NASA videos - Dailymotion"

# Social media Logos XPATH:
Twitter_Logo_XPATH = '//a[@aria-label="Twitter"]'
Facebook_Logo_XPATH = "//div[@class='om3e55n1 cgu29s5g alzwoclg i85zmo3j']"
Instagram_Logo_XPATH = "//body/div[@id='mount_0_0_Wx']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[" \
                       "1]/section[1]/nav[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]/*[1] "
Snapchat_Logo_XPATH = "//body/div[@id='__next']/div[1]/main[1]/div[1]/nav[1]/div[1]/div[1]/a[1]"
YouTube_Logo_XPATH = "//ytd-masthead/div[@id='container']/div[@id='start']/ytd-topbar-logo-renderer[@id='logo']/a[" \
                     "@id='logo']/div[1]/ytd-logo[1]/yt-icon[1] "
Tumblr_Logo_XPATH = '//a[@class="t-logo t-logo--full"]'
Pinterest_Logo_XPATH = "//body/div[@id='__PWS_ROOT__']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[" \
                       "1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1] "
GIPHY_Logo_XPATH = "//span[contains(@class,'_344zAAImiRYcuyn_Nv3HA5 yFb2BrRWgCdRbNnxZap9i')]"
LinkedIn_Logo_XPATH = '//icon[@class="block text-color-brand w-[84px] h-[21px] papabear:w-[135px] papabear:h-[34px] ' \
                      'lazy-loaded"] '
Flickr_Logo_ID = "yui_3_16_0_1_1663035384302_2358"
Twitch_Logo_XPATH = '//figure[@class="ScFigure-sc-cdc1ai-1 hvkYPb"]'
SoundCloud_Logo_XPATH = "//a[contains(@class,'logoLink-wordmark sc-border-box sc-ir')]"
Reddit_Logo_XPATH = '//a[@aria-label="Home"]'
Dailymotion_Logo_XPATH = '//a[@class="Logo__logo___3gjgc Logo__dark___1HMED"]'


# Assert page title:
def assert_title(smt, driver):
    assert smt == driver.title
    print("The Title of the page is:", driver.title)


# Assert Title for back page:
def assert_back_title(driver):
    assert "NASA" == driver.title
    print("Back to the main page")


# Assert title with different attribute:
def check_title(a, driver):
    assert a in driver.title
    print(f'The title of the {a} is:', driver.title)


# Function for switching windows:
def switching_windows(driver):
    wait = WebDriverWait(driver, 3)
    original_window = driver.current_window_handle
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


# Function to check the logo:
def logo_check(smt, path, driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(
            EC.visibility_of_element_located((By.XPATH, path)))
        print(f'We have {smt} logo')
    except WDE:
        print(f'Smt is wrong with {smt} logo')
        driver.get_screenshot_as_file(f'{smt}_logo_loading_error.png')
        driver.save_screenshot(f'{smt}_logo_loading_error.png')


# Function to check specific element on page:
def specific_element_check(smt, path, driver2):
    wait = WebDriverWait(driver2, 3)
    wait.until(EC.visibility_of_element_located(By.XPATH))


print(f'Specific element was found')
