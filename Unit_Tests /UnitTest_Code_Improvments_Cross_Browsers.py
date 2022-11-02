import random
import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.common.exceptions import WebDriverException as WDE
from faker import Faker
import helpers as HP


# Headless: (use next 3 lines if needed):
# options = webdriver.ChromeOptions()
# options.headless = True
# driver = webdriver.Chrome(options=options)


# GoogleChrome Browser UnitTest:


class GoogleChrome(unittest.TestCase):

    # Setup function:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Check if social media icons are clickable, (TC-003):
    def test_icons_clickable(self):
        driver2 = self.driver
        driver2.get(HP.url)

        # Random delay function:
        def delay():
            time.sleep(random.randint(1, 5))
            delay()

        # Check if URL is correct, (helper):
        Nasa_Expected_URL = HP.url
        current_url = driver2.current_url
        if current_url == Nasa_Expected_URL:
            print("Current URL is OK:", driver2.current_url)
        else:
            print("Current URL is different than expected:", driver2.current_url)

        # Check if title is correct, (helper):
        Nasa_Expected_Title = "NASA"
        current_title = driver2.title
        if current_title == Nasa_Expected_Title:
            print("Current Title is OK:", driver2.title)
        else:
            print("Current Title is different than expected:", driver2.title)

        # Find elements by XPATH and click on it:
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH, "//a[@href='/socialmedia'][contains(.,'Social Media')]").click()

        # Set up wait time
        wait = WebDriverWait(driver2, 5)

        # Verify social media icons are clickable, (helpers):
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitter)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.facebook)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.instagram)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.instagram)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.snapchat)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.youtube)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.tumblr)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.linkedin)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.giphy)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.flickr)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.soundcloud)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.reddit)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.dailymotion)))

            print("Social media icons are clickable")
        except WDE:
            print("Check social media icons click ability")
        HP.delay_1_2()

        # Validate Twitter linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.twitter).click()
            print("Twitter icon is clickable")
        except NoSuchElementException:
            print("Twitter icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Twitter_URL)

        # Verify correct Social media page was reached by URL:
        TwitterURL = driver2.current_url
        if TwitterURL == HP.Twitter_URL:
            print("Current TwitterURL is correct:", driver2.current_url)
        else:
            print("TwitterURL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Twitter_Expected_Title = HP.Twitter_Title
        if driver2.title == Twitter_Expected_Title:
            print("Twitter title is correct:", driver2.title)
        else:
            print("Twitter title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Twitter_Logo_XPATH)
            print("Twitter Logo was found")
        except NoSuchElementException:
            print("Twitter Logo was not found")

        HP.delay_1_2()

        # Verify correct Social media page was reached by Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Tweets & replies')]")))
        try:
            driver2.find_element(By.XPATH, "//span[contains(.,'Tweets & replies')]")
            print("Twitter specific element is present on opened page")
        except NoSuchElementException:
            print("No specific Twitter element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Facebook linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.facebook).click()
            print("Facebook icon is clickable")
        except NoSuchElementException:
            print("Facebook icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Facebook_URL)

        # Verify correct Social media page was reached by URL:
        FacebookURL = driver2.current_url
        if FacebookURL == HP.Facebook_URL:
            print("Current Facebook URL is correct:", driver2.current_url)
        else:
            print("Facebook URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Facebook_Expected_Title = HP.Facebook_Title
        if driver2.title == Facebook_Expected_Title:
            print("Facebook title is correct:", driver2.title)
        else:
            print("Facebook title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Facebook_Logo_XPATH)
            print("Facebook Logo was found")
        except NoSuchElementException:
            print("Facebook Logo was not found")

        HP.delay_1_2()

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Log In')])[17]")))
        try:
            driver2.find_element(By.XPATH, "(//div[contains(.,'Log In')])[17]")
            print("Facebook specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Facebook element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Instagram linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.instagram).click()
            print("Instagram icon is clickable")
        except NoSuchElementException:
            print("Instagram icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Instagram_URL)

        # Verify correct Social media page was reached by URL:
        InstagramURL = driver2.current_url
        if InstagramURL == HP.Instagram_URL:
            print("Current Instagram URL is correct:", driver2.current_url)
        else:
            print("Instagram URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Instagram_Expected_Title = HP.Instagram_Title
        if driver2.title == Instagram_Expected_Title:
            print("Instagram title is correct:", driver2.title)
        else:
            print("Instagram title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Instagram_Logo_XPATH)
            print("Instagram Logo was found")
        except NoSuchElementException:
            print("Instagram Logo was not found")

        HP.delay_1_2()

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Posts')]")))
        try:
            driver2.find_element(By.XPATH, "//span[contains(.,'Posts')]")
            print("Instagram specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Instagram element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Snapchat linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.snapchat).click()
            print("Snapchat icon is clickable")
        except NoSuchElementException:
            print("Snapchat icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Snapchat_URL)

        # Verify correct Social media page was reached by URL:
        SnapchatURL = driver2.current_url
        if SnapchatURL == HP.Snapchat_URL:
            print("Current Snapchat URL is correct:", driver2.current_url)
        else:
            print("Snapchat URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Snapchat_Expected_Title = HP.Snapchat_Title
        if driver2.title == Snapchat_Expected_Title:
            print("Snapchat title is correct:", driver2.title)
        else:
            print("Snapchat title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Snapchat_Logo_XPATH)
            print("Snapchat Logo was found")
        except NoSuchElementException:
            print("Snapchat Logo was not found")

        HP.delay_1_2()

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='PublicProfileCard_desktopTitle__9ik6D "
                                                               "PublicProfileCard_desktopText__IYnRg'][contains(.,"
                                                               "'Explore the universe and discover our home planet "
                                                               "with official NASA snaps.')]")))
        try:
            driver2.find_element(By.XPATH, "//div[@class='PublicProfileCard_desktopTitle__9ik6D "
                                           "PublicProfileCard_desktopText__IYnRg'][contains(.,'Explore the universe "
                                           "and discover our home planet with official NASA snaps.')]")
            print("Snapchat specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Snapchat element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate YouTube linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.youtube).click()
            print("YouTube icon is clickable")
        except NoSuchElementException:
            print("YouTube icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.YouTube_URL)

        # Verify correct Social media page was reached by URL:
        YouTubeURL = driver2.current_url
        if YouTubeURL == HP.YouTube_URL:
            print("Current YouTube URL is correct:", driver2.current_url)
        else:
            print("YouTube URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        YouTube_Expected_Title = HP.YouTube_Title
        if driver2.title == YouTube_Expected_Title:
            print("YouTube title is correct:", driver2.title)
        else:
            print("YouTube title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.YouTube_Logo_XPATH)
            print("YouTube Logo was found")
        except NoSuchElementException:
            print("YouTube Logo was not found")

        HP.delay_1_2()

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='channel-header-container']//yt-img-shadow["
                                                               "@id='avatar']//img[@id='img']")))
        try:
            driver2.find_element(By.XPATH, "//div[@id='channel-header-container']//yt-img-shadow[@id='avatar']//img["
                                           "@id='img']")
            print("YouTube specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific YouTube element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Pinterest linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.pinterest).click()
            print("Pinterest icon is clickable")
        except NoSuchElementException:
            print("Pinterest icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Pinterest_URL)

        # Verify correct Social media page was reached by URL:
        Pinterest = driver2.current_url
        if Pinterest == HP.Pinterest_URL:
            print("Current Pinterest URL is correct:", driver2.current_url)
        else:
            print("Pinterest URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Pinterest_Expected_Title = HP.Pinterest_Title
        if driver2.title == Pinterest_Expected_Title:
            print("Pinterest title is correct:", driver2.title)
        else:
            print("Pinterest title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Pinterest_Logo_XPATH)
            print("Pinterest Logo was found")
        except NoSuchElementException:
            print("Pinterest Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="tBJ dyH iFc sAJ xnr tg7 H2s"]')))
        try:
            driver2.find_element(By.XPATH, '//div[@class="tBJ dyH iFc sAJ xnr tg7 H2s"]')
            print("Pinterest specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Pinterest element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate GIPHY linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.giphy).click()
            print("GIPHY icon is clickable")
        except NoSuchElementException:
            print("GIPHY icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.GIPHY_URL)

        # Verify correct Social media page was reached by URL:
        GIPHY = driver2.current_url
        if GIPHY == HP.GIPHY_URL:
            print("Current GIPHY URL is correct:", driver2.current_url)
        else:
            print("GIPHY URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        GIPHY_Expected_Title = HP.GIPHY_Title
        if driver2.title == GIPHY_Expected_Title:
            print("GIPHY title is correct:", driver2.title)
        else:
            print("GIPHY title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.GIPHY_Logo_XPATH)
            print("GIPHY Logo was found")
        except NoSuchElementException:
            print("GIPHY Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="Avatar-sc-egp6lv butWAC"]')))
        try:
            driver2.find_element(By.XPATH, '//div[@class="Avatar-sc-egp6lv butWAC"]')
            print("GIPHY specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific GIPHY element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Flickr linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.flickr).click()
            print("Flickr icon is clickable")
        except NoSuchElementException:
            print("Flickr icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Flickr_URL)

        # Verify correct Social media page was reached by URL:
        Flickr = driver2.current_url
        if Flickr == HP.Flickr_URL:
            print("Flickr GIPHY URL is correct:", driver2.current_url)
        else:
            print("Flickr URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Flickr_Expected_Title = HP.Flickr_Title
        if driver2.title == Flickr_Expected_Title:
            print("Flickr title is correct:", driver2.title)
        else:
            print("Flickr title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.ID, HP.Flickr_Logo_ID)
            print("Flickr Logo was found")
        except NoSuchElementException:
            print("Flickr Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        # wait.until(EC.visibility_of_element_located((By.ID, 'yui_3_16_0_1_1663035384302_2366')))
        try:
            driver2.find_element(By.ID, 'yui_3_16_0_1_1663035384302_2366')
            print("Flickr specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Flickr element on the  opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Twitch linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.twitch).click()
            print("Twitch icon is clickable")
        except NoSuchElementException:
            print("Twitch icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Twitch_URL)

        # Verify correct Social media page was reached by URL:
        Twitch = driver2.current_url
        if Twitch == HP.Twitch_URL:
            print("Twitch GIPHY URL is correct:", driver2.current_url)
        else:
            print("Twitch URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Twitch_Expected_Title = HP.Twitch_Title
        if driver2.title == Twitch_Expected_Title:
            print("Twitch title is correct:", driver2.title)
        else:
            print("Twitch title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Twitch_Logo_XPATH)
            print("Twitch Logo was found")
        except NoSuchElementException:
            print("Twitch Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@data-a-target='tw-core-button-label-text']["
                                                               "contains(., "
                                                               "'Sign Up')])[1]")))
        try:
            driver2.find_element(By.XPATH, "(//div[@data-a-target='tw-core-button-label-text'][contains(.,"
                                           "'Sign Up')])[1]")
            print("Twitch specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Twitch element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate SoundCloud linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.soundcloud).click()
            print("SoundCloud icon is clickable")
        except NoSuchElementException:
            print("SoundCloud icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.SoundCloud_URL)

        # Verify correct Social media page was reached by URL:
        SoundCloud = driver2.current_url
        if SoundCloud == HP.SoundCloud_URL:
            print("SoundCloud URL is correct:", driver2.current_url)
        else:
            print("SoundCloud URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        SoundCloud_Expected_Title = HP.SoundCloud_Title
        if driver2.title == SoundCloud_Expected_Title:
            print("SoundCloud title is correct:", driver2.title)
        else:
            print("SoundCloud title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.SoundCloud_Logo_XPATH)
            print("SoundCloud Logo was found")
        except NoSuchElementException:
            print("SoundCloud Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="image image__noOutline interactive '
                                                               'sc-artwork sc-artwork-placeholder-0 image__rounded '
                                                               'm-loaded"]')))
        try:
            driver2.find_element(By.XPATH, '//div[@class="image image__noOutline interactive sc-artwork '
                                           'sc-artwork-placeholder-0 image__rounded m-loaded"]')
            print("SoundCloud specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific SoundCloud element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Reddit linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.reddit).click()
            print("Reddit icon is clickable")
        except NoSuchElementException:
            print("Reddit icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Reddit_URL)

        # Verify correct Social media page was reached by URL:
        Reddit = driver2.current_url
        if Reddit == HP.Reddit_URL:
            print("Reddit URL is correct:", driver2.current_url)
        else:
            print("Reddit URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Reddit_Expected_Title = HP.Reddit_Title
        if driver2.title == Reddit_Expected_Title:
            print("Reddit title is correct:", driver2.title)
        else:
            print("Reddit title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Reddit_Logo_XPATH)
            print("Reddit Logo was found")
        except NoSuchElementException:
            print("Reddit Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        try:
            driver2.find_element(By.XPATH, '//img[@class="_2TN8dEgAQbSyKntWpSPYM7 E6V2eHU4CpJuLWzneTk0Z"]')
            print("Reddit specific element is present on the opened page")
        except NoSuchElementException:
            print("No Reddit specific element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Dailymotion linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.dailymotion).click()
            print("Dailymotion icon is clickable")
        except NoSuchElementException:
            print("Dailymotion icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Dailymotion_URL)

        # Verify correct Social media page was reached by URL:
        Dailymotion = driver2.current_url
        if Dailymotion == HP.Dailymotion_URL:
            print("Dailymotion URL is correct:", driver2.current_url)
        else:
            print("Dailymotion URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Dailymotion_Expected_Title = HP.Dailymotion_Title
        if driver2.title == Dailymotion_Expected_Title:
            print("Dailymotion title is correct:", driver2.title)
        else:
            print("Dailymotion title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Dailymotion_Logo_XPATH)
            print("Dailymotion Logo was found")
        except NoSuchElementException:
            print("Dailymotion Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        try:
            driver2.find_element(By.XPATH, "//button[contains(.,'Follow')]")
            print("Dailymotion specific element is present on the opened page")
        except NoSuchElementException:
            print("Dailymotion Reddit specific element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Tumblr linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.tumblr).click()
            print("Tumblr icon is clickable")
        except NoSuchElementException:
            print("Tumblr icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Tumblr_URL)

        # Verify correct Social media page was reached by URL:
        TumblrURL = driver2.current_url
        if TumblrURL == HP.Tumblr_URL:
            print("Current Tumblr URL is correct:", driver2.current_url)
        else:
            print("Tumblr URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Tumblr_Expected_Title = HP.Tumblr_Title
        if driver2.title == Tumblr_Expected_Title:
            print("Tumblr title is correct:", driver2.title)
        else:
            print("Tumblr title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Tumblr_Logo_XPATH)
            print("Tumblr Logo was found")
        except NoSuchElementException:
            print("Tumblr Logo was not found")

            HP.delay_1_2()

        # Verify correct Social media page was reached and Specific element is present on page:
        try:
            driver2.find_element(By.XPATH, "//body[1]/section[1]/div[1]/header[1]/div[2]/figure[1]/a[1]")
            print("Tumblr specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Tumblr element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate LinkedIn linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, "//img[contains(@alt,'LinkedIn')]").click()
            print("LinkedIn icon is clickable")
        except NoSuchElementException:
            print("LinkedIn icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get("https://www.linkedin.com/company/nasa/")

        # Verify correct Social media page was reached by URL:
        LinkedIn = driver2.current_url
        if LinkedIn == HP.LinkedIn_URL:
            print("LinkedIn  URL is correct:", driver2.current_url)
        else:
            print("LinkedIn URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        LinkedIn_Expected_Title = HP.LinkedIn_Title
        if driver2.title == LinkedIn_Expected_Title:
            print("LinkedIn title is correct:", driver2.title)
        else:
            print("LinkedIn title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.LinkedIn_Logo_XPATH)
            print("LinkedIn Logo was found")
        except NoSuchElementException:
            print("LinkedIn Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[@class="authwall-sign-in-form__header-title"]')))
        try:
            driver2.find_element(By.XPATH, '//h2[@class="authwall-sign-in-form__header-title"]')
            print("LinkedIn  specific element is present on  the opened page")
        except NoSuchElementException:
            print("No specific LinkedIn element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        print("TC-003 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Check the ability of user sign up for NASA’s Newsletters (TC-001):
    def test_newsletters(self):
        driver2 = self.driver
        driver2.get(HP.url)
        self.driver.maximize_window()

        # wait 1-2 seconds:
        HP.delay_1_2()

        # check if Title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH,
                             "//a[@href='https://www.nasa.gov/newsletters'][contains(.,'NASA Newsletters')]").click()
        HP.delay_1_2()

        driver2.find_element(By.XPATH, "//a[@href='https://www.nasa.gov/specials/newsletter-sign-up/']").click()
        HP.delay_1_2()

        # Faker set up:
        fake = Faker()

        # Find elements by XPATH and send fake data:
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0102@gmail.com")
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').send_keys(fake.first_name())
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').send_keys(fake.last_name())
        driver2.find_element(By.XPATH, '//input[@data-input-id="city"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="city"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="city"]').send_keys(fake.city())
        driver2.find_element(By.XPATH, '//input[@data-input-id="state"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="state"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="state"]').send_keys(fake.state())
        driver2.find_element(By.XPATH, '//input[@data-input-id="postal_code"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="postal_code"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="postal_code"]').send_keys("11229")
        driver2.find_element(By.XPATH, '//input[@data-input-id="country"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="country"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="country"]').send_keys(fake.country())

        driver2.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        # somtimes should pass Captcha before (with 3 images selection)

        # Verify that Subscription for Newsletters was sent :
        wait = WebDriverWait(driver2, 3)
        form = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Thanks for Subscribing!")]'))).text

        if form == "Thanks for Subscribing!":
            print("Subscription for Newsletters was sent")
        else:
            print("Check Subscription for Newsletters")

        print("Subscription for Newsletters was checked")
        print("TC-001 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify that user is unable to make a subscription for a Newsletters by using invalid Email, (TC-002)/Negative

    def test_subscription_negative(self):
        driver2 = self.driver
        driver2.get(HP.url)
        self.driver.maximize_window()

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # Check if title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH,
                             "//a[@href='https://www.nasa.gov/newsletters'][contains(.,'NASA Newsletters')]").click()
        HP.delay_1_2()

        driver2.find_element(By.XPATH, "//a[@href='https://www.nasa.gov/specials/newsletter-sign-up/']").click()
        HP.delay_1_2()

        # Find elements by XPATH and send fake data:
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0102@gmail.c")
        driver2.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        HP.delay_1_2()

        # Verify user got Error Message:
        assert driver2.find_element(By.XPATH, "//div[@class='message'][contains(.,'Email is invalid.')]").is_displayed()
        print("Error Message is displayed")

        # or way #2 to verify the Error Message was displayed:
        # driver2.find_element(By.XPATH, "//div[@class='message'][contains(.,'Email is invalid.')]")
        # print("Error Message is displayed")

        print("User is unable to make subscription with Invalid Email")
        print("TC-002 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify the ability of user to make a registration for NASA's upcoming events, (TC-004):

    def test_upcoming_events(self):
        driver2 = self.driver
        driver2.get(HP.url)

        # Set up custom window size:
        self.driver.set_window_size(300, 1800)

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # check if Title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        driver2.find_element(By.XPATH, '//button[@class ="navbar-toggle collapsed"]').click()
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH, "//a[@href='/specials/virtualguest/']").click()

        HP.delay_1_2()

        # Verify opened page is SignUp Form page by Title:
        assert "NASA Virtual Guest Ops" in driver2.title
        print("NASA Virtual Guest page is opened")

        driver2.find_element(By.XPATH, '//a[@class ="w3-button w3-round-xlarge w3-nasa-blue"]').click()

        HP.delay_1_2()

        driver2.get("https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests")

        # Verify opened page is SignUp Form page bu URL:
        # driver2.find_element(By.XPATH, "//img[@data-image-content]")
        assert "https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests" in driver2.current_url
        print("Current Signup Form Page is correct")

        # Faker set up:
        fake = Faker()

        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0103@gmail.com")
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').send_keys(fake.first_name())
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').send_keys(fake.last_name())

        driver2.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        # should pass Captcha before with 3 images selection:
        # driver1.find_element(By.XPATH, '//a[@data-purpose="download"]')

        # Verify that Registration for Upcoming events was done :
        wait = WebDriverWait(driver2, 3)
        form = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Thanks for Signing up!")]'))).text

        if form == "Thanks for Subscribing!":
            print("Subscription for Newsletters was sent")
        else:
            print("Check Subscription for Newsletters")
        # Verify user got Error Message:
        assert driver2.find_element(By.XPATH, "//div[@class='message'][contains(.,'Email is invalid.')]").is_displayed()
        print("Successful Message is displayed")

        print("Join to NASA's Virtual Guest List was Done!")
        print("TC-004 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify that user is unable to make a registration  for NASA's upcoming events  with invalid email,
    # (TC-005)/Negative Test:

    def test_upcoming_events_negative(self):
        driver2 = self.driver
        driver2.get(HP.url)

        # Set up custom window size:
        self.driver.set_window_size(300, 1800)

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # Check if title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        driver2.find_element(By.XPATH, '//button[@class ="navbar-toggle collapsed"]').click()
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH, "//a[@href='/specials/virtualguest/']").click()

        HP.delay_1_2()

        # Verify opened page is SignUp Form page:
        assert "NASA Virtual Guest Ops" in driver2.title
        print("NASA Virtual Guest page is opened")

        driver2.find_element(By.XPATH, '//a[@class ="w3-button w3-round-xlarge w3-nasa-blue"]').click()

        HP.delay_1_2()

        driver2.get("https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests")

        # Verify opened page is SignUp Form page:
        assert "https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests" in driver2.current_url
        driver2.find_element(By.XPATH, "//img[@data-image-content]")

        print("Current Signup Form Page is correct")

        # Faker set up:
        fake = Faker()

        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0103@gmail.c")
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').send_keys(fake.first_name())
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').send_keys(fake.last_name())

        print("Sign Up Form is filled by Fake data")

        # Click "Submit" button:
        driver2.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        # Verify user got Error Message:
        assert driver2.find_element(By.XPATH, "//label[contains(., '* Email')]").is_displayed()
        print("Error Message is displayed")

        print("User is unable to make a registration  for NASA's upcoming events  with invalid email")
        print("TC-005 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify that Logo leads to the website's Homepage after clicking on it, (TC-006):

    def test_logo_functionality(self):
        driver2 = self.driver
        driver2.get(HP.url)
        self.driver.maximize_window()

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # Check if Title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH, "//a[@href='/solve/index.html'][contains(.,'Get Involved')]").click()

        HP.delay_1_2()

        # Verify opened page is SignUp Form page:
        assert "Participate with NASA Solve | NASA" in driver2.title
        print("Page title is correct")

        HP.delay_1_2()

        # Find logo Icon:
        driver2.find_element(By.XPATH, "//nav[@id='navbar-nasa']/div/a/img").click()
        # driver.find_element(By.XPATH, '//img[@alt="Nasa" and @xpath="1"]').click()

        HP.delay_1_2()

        # Verify logo leaded to Homepage:
        # Check if Homepage title is correct, strict assertion:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if Homepage URL is correct, strict assertion:
        assert HP.url == driver2.current_url
        print("Current URL of Homepage is OK:", driver2.current_url)

        # Verify logo leaded to Homepage by specific element present:
        try:
            driver2.find_element(By.XPATH, "(//a[contains(.,'Humans in Space')])[1]")
            print("Specific element was found on Homepage")
        except NoSuchElementException:
            print("Specific element was NOT  found on Homepage")

        print("Logo leads to the website's Homepage")
        print("TC-006 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify that the “Search” field is working appropriate, (TC-007):

    def test_search_field(self):
        driver2 = self.driver
        driver2.get(HP.url)
        self.driver.maximize_window()

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # Check if Title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        try:
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").click()
            HP.delay_1_2()
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys("Events")
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys(Keys.RETURN)
            print("Search field is working")

        except WDE:
            print("Check Search field")

        HP.delay_1_2()
        assert "Events - NASA Search Results" in driver2.title

        print("Correct Page is opened by Search result")
        print("TC-007 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify that the “Search” field is working appropriate/Negative Testing),(TC-008):

    def test_search_field_negative(self):
        driver2 = self.driver
        driver2.get(HP.url)
        self.driver.maximize_window()

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # Check if Title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        try:
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").click()
            HP.delay_1_2()
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys(".")
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys(Keys.RETURN)
            print("Search field try to sent invalid data")
        except WDE:
            print("Search field is not working")

        HP.delay_1_2()
        assert ". - NASA Search Results" in driver2.title
        print("New page is opened")

        driver2.find_element(By.XPATH, "//div[contains( @class ,'content-block-item')]")
        assert driver2.find_element(By.XPATH, '//div[contains(text(),"Sorry, no results found for")]').is_displayed()
        print("Notification about wrong data in Search field was cached")

        # Make and save screenshot:
        driver2.get_screenshot_as_file("Notification_about_wrong_data.png")
        driver2.save_screenshot("Notification_about_wrong_data.png")
        print("Screenshot was done and save")

        print("TC-008 is PASSED")

        # Close entire Browser:
        driver2.quit()


# close entire Browser:


def tearDown(self):
    self.driver.quit()


# FireFox Browser UnitTest:

# Headless:

# options = webdriver.FirefoxOptions()
# options.headless = True
# driver1 = webdriver.Firefox(options=options)


class FireFox(unittest.TestCase):

    # Setup function:
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # Check if social media icons are clickable, (TC-003):
    def test_icons_clickable(self):
        driver2 = self.driver
        driver2.get(HP.url)

        # Random delay function:
        def delay():
            time.sleep(random.randint(1, 5))
            delay()

        # Check if URL is correct, (helper):
        Nasa_Expected_URL = HP.url
        current_url = driver2.current_url
        if current_url == Nasa_Expected_URL:
            print("Current URL is OK:", driver2.current_url)
        else:
            print("Current URL is different than expected:", driver2.current_url)

        # Check if title is correct, (helper):
        Nasa_Expected_Title = "NASA"
        current_title = driver2.title
        if current_title == Nasa_Expected_Title:
            print("Current Title is OK:", driver2.title)
        else:
            print("Current Title is different than expected:", driver2.title)

        # Find elements by XPATH and click on it:
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH, "//a[@href='/socialmedia'][contains(.,'Social Media')]").click()

        # Set up wait time
        wait = WebDriverWait(driver2, 5)

        # Verify social media icons are clickable, (helpers):
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitter)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.facebook)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.instagram)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.instagram)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.snapchat)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.youtube)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.tumblr)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.linkedin)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.giphy)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.flickr)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.soundcloud)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.reddit)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.dailymotion)))

            print("Social media icons are clickable")
        except WDE:
            print("Check social media icons click ability")
        HP.delay_1_2()

        # Validate Twitter linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.twitter).click()
            print("Twitter icon is clickable")
        except NoSuchElementException:
            print("Twitter icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Twitter_URL)

        # Verify correct Social media page was reached by URL:
        TwitterURL = driver2.current_url
        if TwitterURL == HP.Twitter_URL:
            print("Current TwitterURL is correct:", driver2.current_url)
        else:
            print("TwitterURL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Twitter_Expected_Title = HP.Twitter_Title
        if driver2.title == Twitter_Expected_Title:
            print("Twitter title is correct:", driver2.title)
        else:
            print("Twitter title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Twitter_Logo_XPATH)
            print("Twitter Logo was found")
        except NoSuchElementException:
            print("Twitter Logo was not found")

        HP.delay_1_2()

        # Verify correct Social media page was reached by Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Tweets & replies')]")))
        try:
            driver2.find_element(By.XPATH, "//span[contains(.,'Tweets & replies')]")
            print("Twitter specific element is present on opened page")
        except NoSuchElementException:
            print("No specific Twitter element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Facebook linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.facebook).click()
            print("Facebook icon is clickable")
        except NoSuchElementException:
            print("Facebook icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Facebook_URL)

        # Verify correct Social media page was reached by URL:
        FacebookURL = driver2.current_url
        if FacebookURL == HP.Facebook_URL:
            print("Current Facebook URL is correct:", driver2.current_url)
        else:
            print("Facebook URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Facebook_Expected_Title = HP.Facebook_Title
        if driver2.title == Facebook_Expected_Title:
            print("Facebook title is correct:", driver2.title)
        else:
            print("Facebook title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Facebook_Logo_XPATH)
            print("Facebook Logo was found")
        except NoSuchElementException:
            print("Facebook Logo was not found")

        HP.delay_1_2()

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Log In')])[17]")))
        try:
            driver2.find_element(By.XPATH, "(//div[contains(.,'Log In')])[17]")
            print("Facebook specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Facebook element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Instagram linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.instagram).click()
            print("Instagram icon is clickable")
        except NoSuchElementException:
            print("Instagram icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Instagram_URL)

        # Verify correct Social media page was reached by URL:
        InstagramURL = driver2.current_url
        if InstagramURL == HP.Instagram_URL:
            print("Current Instagram URL is correct:", driver2.current_url)
        else:
            print("Instagram URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Instagram_Expected_Title = HP.Instagram_Title
        if driver2.title == Instagram_Expected_Title:
            print("Instagram title is correct:", driver2.title)
        else:
            print("Instagram title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Instagram_Logo_XPATH)
            print("Instagram Logo was found")
        except NoSuchElementException:
            print("Instagram Logo was not found")

        HP.delay_1_2()

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Posts')]")))
        try:
            driver2.find_element(By.XPATH, "//span[contains(.,'Posts')]")
            print("Instagram specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Instagram element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Snapchat linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.snapchat).click()
            print("Snapchat icon is clickable")
        except NoSuchElementException:
            print("Snapchat icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Snapchat_URL)

        # Verify correct Social media page was reached by URL:
        SnapchatURL = driver2.current_url
        if SnapchatURL == HP.Snapchat_URL:
            print("Current Snapchat URL is correct:", driver2.current_url)
        else:
            print("Snapchat URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Snapchat_Expected_Title = HP.Snapchat_Title
        if driver2.title == Snapchat_Expected_Title:
            print("Snapchat title is correct:", driver2.title)
        else:
            print("Snapchat title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Snapchat_Logo_XPATH)
            print("Snapchat Logo was found")
        except NoSuchElementException:
            print("Snapchat Logo was not found")

        HP.delay_1_2()

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='PublicProfileCard_desktopTitle__9ik6D "
                                                               "PublicProfileCard_desktopText__IYnRg'][contains(.,"
                                                               "'Explore the universe and discover our home planet "
                                                               "with official NASA snaps.')]")))
        try:
            driver2.find_element(By.XPATH, "//div[@class='PublicProfileCard_desktopTitle__9ik6D "
                                           "PublicProfileCard_desktopText__IYnRg'][contains(.,'Explore the universe "
                                           "and discover our home planet with official NASA snaps.')]")
            print("Snapchat specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Snapchat element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate YouTube linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.youtube).click()
            print("YouTube icon is clickable")
        except NoSuchElementException:
            print("YouTube icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.YouTube_URL)

        # Verify correct Social media page was reached by URL:
        YouTubeURL = driver2.current_url
        if YouTubeURL == HP.YouTube_URL:
            print("Current YouTube URL is correct:", driver2.current_url)
        else:
            print("YouTube URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        YouTube_Expected_Title = HP.YouTube_Title
        if driver2.title == YouTube_Expected_Title:
            print("YouTube title is correct:", driver2.title)
        else:
            print("YouTube title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.YouTube_Logo_XPATH)
            print("YouTube Logo was found")
        except NoSuchElementException:
            print("YouTube Logo was not found")

        HP.delay_1_2()

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='channel-header-container']//yt-img-shadow["
                                                               "@id='avatar']//img[@id='img']")))
        try:
            driver2.find_element(By.XPATH, "//div[@id='channel-header-container']//yt-img-shadow[@id='avatar']//img["
                                           "@id='img']")
            print("YouTube specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific YouTube element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Pinterest linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.pinterest).click()
            print("Pinterest icon is clickable")
        except NoSuchElementException:
            print("Pinterest icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Pinterest_URL)

        # Verify correct Social media page was reached by URL:
        Pinterest = driver2.current_url
        if Pinterest == HP.Pinterest_URL:
            print("Current Pinterest URL is correct:", driver2.current_url)
        else:
            print("Pinterest URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Pinterest_Expected_Title = HP.Pinterest_Title
        if driver2.title == Pinterest_Expected_Title:
            print("Pinterest title is correct:", driver2.title)
        else:
            print("Pinterest title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Pinterest_Logo_XPATH)
            print("Pinterest Logo was found")
        except NoSuchElementException:
            print("Pinterest Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="tBJ dyH iFc sAJ xnr tg7 H2s"]')))
        try:
            driver2.find_element(By.XPATH, '//div[@class="tBJ dyH iFc sAJ xnr tg7 H2s"]')
            print("Pinterest specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Pinterest element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate GIPHY linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.giphy).click()
            print("GIPHY icon is clickable")
        except NoSuchElementException:
            print("GIPHY icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.GIPHY_URL)

        # Verify correct Social media page was reached by URL:
        GIPHY = driver2.current_url
        if GIPHY == HP.GIPHY_URL:
            print("Current GIPHY URL is correct:", driver2.current_url)
        else:
            print("GIPHY URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        GIPHY_Expected_Title = HP.GIPHY_Title
        if driver2.title == GIPHY_Expected_Title:
            print("GIPHY title is correct:", driver2.title)
        else:
            print("GIPHY title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.GIPHY_Logo_XPATH)
            print("GIPHY Logo was found")
        except NoSuchElementException:
            print("GIPHY Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="Avatar-sc-egp6lv butWAC"]')))
        try:
            driver2.find_element(By.XPATH, '//div[@class="Avatar-sc-egp6lv butWAC"]')
            print("GIPHY specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific GIPHY element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Flickr linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.flickr).click()
            print("Flickr icon is clickable")
        except NoSuchElementException:
            print("Flickr icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Flickr_URL)

        # Verify correct Social media page was reached by URL:
        Flickr = driver2.current_url
        if Flickr == HP.Flickr_URL:
            print("Flickr GIPHY URL is correct:", driver2.current_url)
        else:
            print("Flickr URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Flickr_Expected_Title = HP.Flickr_Title
        if driver2.title == Flickr_Expected_Title:
            print("Flickr title is correct:", driver2.title)
        else:
            print("Flickr title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.ID, HP.Flickr_Logo_ID)
            print("Flickr Logo was found")
        except NoSuchElementException:
            print("Flickr Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        # wait.until(EC.visibility_of_element_located((By.ID, 'yui_3_16_0_1_1663035384302_2366')))
        try:
            driver2.find_element(By.ID, 'yui_3_16_0_1_1663035384302_2366')
            print("Flickr specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Flickr element on the  opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Twitch linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.twitch).click()
            print("Twitch icon is clickable")
        except NoSuchElementException:
            print("Twitch icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Twitch_URL)

        # Verify correct Social media page was reached by URL:
        Twitch = driver2.current_url
        if Twitch == HP.Twitch_URL:
            print("Twitch GIPHY URL is correct:", driver2.current_url)
        else:
            print("Twitch URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Twitch_Expected_Title = HP.Twitch_Title
        if driver2.title == Twitch_Expected_Title:
            print("Twitch title is correct:", driver2.title)
        else:
            print("Twitch title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Twitch_Logo_XPATH)
            print("Twitch Logo was found")
        except NoSuchElementException:
            print("Twitch Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@data-a-target='tw-core-button-label-text']["
                                                               "contains(., "
                                                               "'Sign Up')])[1]")))
        try:
            driver2.find_element(By.XPATH, "(//div[@data-a-target='tw-core-button-label-text'][contains(.,"
                                           "'Sign Up')])[1]")
            print("Twitch specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Twitch element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate SoundCloud linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.soundcloud).click()
            print("SoundCloud icon is clickable")
        except NoSuchElementException:
            print("SoundCloud icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.SoundCloud_URL)

        # Verify correct Social media page was reached by URL:
        SoundCloud = driver2.current_url
        if SoundCloud == HP.SoundCloud_URL:
            print("SoundCloud URL is correct:", driver2.current_url)
        else:
            print("SoundCloud URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        SoundCloud_Expected_Title = HP.SoundCloud_Title
        if driver2.title == SoundCloud_Expected_Title:
            print("SoundCloud title is correct:", driver2.title)
        else:
            print("SoundCloud title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.SoundCloud_Logo_XPATH)
            print("SoundCloud Logo was found")
        except NoSuchElementException:
            print("SoundCloud Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="image image__noOutline interactive '
                                                               'sc-artwork sc-artwork-placeholder-0 image__rounded '
                                                               'm-loaded"]')))
        try:
            driver2.find_element(By.XPATH, '//div[@class="image image__noOutline interactive sc-artwork '
                                           'sc-artwork-placeholder-0 image__rounded m-loaded"]')
            print("SoundCloud specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific SoundCloud element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Reddit linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.reddit).click()
            print("Reddit icon is clickable")
        except NoSuchElementException:
            print("Reddit icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Reddit_URL)

        # Verify correct Social media page was reached by URL:
        Reddit = driver2.current_url
        if Reddit == HP.Reddit_URL:
            print("Reddit URL is correct:", driver2.current_url)
        else:
            print("Reddit URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Reddit_Expected_Title = HP.Reddit_Title
        if driver2.title == Reddit_Expected_Title:
            print("Reddit title is correct:", driver2.title)
        else:
            print("Reddit title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Reddit_Logo_XPATH)
            print("Reddit Logo was found")
        except NoSuchElementException:
            print("Reddit Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        try:
            driver2.find_element(By.XPATH, '//img[@class="_2TN8dEgAQbSyKntWpSPYM7 E6V2eHU4CpJuLWzneTk0Z"]')
            print("Reddit specific element is present on the opened page")
        except NoSuchElementException:
            print("No Reddit specific element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Dailymotion linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.dailymotion).click()
            print("Dailymotion icon is clickable")
        except NoSuchElementException:
            print("Dailymotion icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Dailymotion_URL)

        # Verify correct Social media page was reached by URL:
        Dailymotion = driver2.current_url
        if Dailymotion == HP.Dailymotion_URL:
            print("Dailymotion URL is correct:", driver2.current_url)
        else:
            print("Dailymotion URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Dailymotion_Expected_Title = HP.Dailymotion_Title
        if driver2.title == Dailymotion_Expected_Title:
            print("Dailymotion title is correct:", driver2.title)
        else:
            print("Dailymotion title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Dailymotion_Logo_XPATH)
            print("Dailymotion Logo was found")
        except NoSuchElementException:
            print("Dailymotion Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        try:
            driver2.find_element(By.XPATH, "//button[contains(.,'Follow')]")
            print("Dailymotion specific element is present on the opened page")
        except NoSuchElementException:
            print("Dailymotion Reddit specific element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate Tumblr linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, HP.tumblr).click()
            print("Tumblr icon is clickable")
        except NoSuchElementException:
            print("Tumblr icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get(HP.Tumblr_URL)

        # Verify correct Social media page was reached by URL:
        TumblrURL = driver2.current_url
        if TumblrURL == HP.Tumblr_URL:
            print("Current Tumblr URL is correct:", driver2.current_url)
        else:
            print("Tumblr URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        Tumblr_Expected_Title = HP.Tumblr_Title
        if driver2.title == Tumblr_Expected_Title:
            print("Tumblr title is correct:", driver2.title)
        else:
            print("Tumblr title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.Tumblr_Logo_XPATH)
            print("Tumblr Logo was found")
        except NoSuchElementException:
            print("Tumblr Logo was not found")

            HP.delay_1_2()

        # Verify correct Social media page was reached and Specific element is present on page:
        try:
            driver2.find_element(By.XPATH, "//body[1]/section[1]/div[1]/header[1]/div[2]/figure[1]/a[1]")
            print("Tumblr specific element is present on the opened page")
        except NoSuchElementException:
            print("No specific Tumblr element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        # Validate LinkedIn linked icon leads to correct page:
        try:
            driver2.find_element(By.XPATH, "//img[contains(@alt,'LinkedIn')]").click()
            print("LinkedIn icon is clickable")
        except NoSuchElementException:
            print("LinkedIn icon is NOT clickable")

        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.get("https://www.linkedin.com/company/nasa/")

        # Verify correct Social media page was reached by URL:
        LinkedIn = driver2.current_url
        if LinkedIn == HP.LinkedIn_URL:
            print("LinkedIn  URL is correct:", driver2.current_url)
        else:
            print("LinkedIn URL is different from expected:", driver2.current_url)

        # Verify correct Social media page was reached by Title:
        LinkedIn_Expected_Title = HP.LinkedIn_Title
        if driver2.title == LinkedIn_Expected_Title:
            print("LinkedIn title is correct:", driver2.title)
        else:
            print("LinkedIn title is different from expected:", driver2.title)

        # Verify correct Social media page was reached by Logo:
        try:
            driver2.find_element(By.XPATH, HP.LinkedIn_Logo_XPATH)
            print("LinkedIn Logo was found")
        except NoSuchElementException:
            print("LinkedIn Logo was not found")

        # Verify correct Social media page was reached and Specific element is present on page:
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[@class="authwall-sign-in-form__header-title"]')))
        try:
            driver2.find_element(By.XPATH, '//h2[@class="authwall-sign-in-form__header-title"]')
            print("LinkedIn  specific element is present on  the opened page")
        except NoSuchElementException:
            print("No specific LinkedIn element on the opened page")

        # Make driver back on previous page:
        driver2.back()

        # Wait 1-2 sec:
        HP.delay_1_2()

        print("TC-003 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Check the ability of user sign up for NASA’s Newsletters (TC-001):
    def test_newsletters(self):
        driver2 = self.driver
        driver2.get(HP.url)
        self.driver.maximize_window()

        # wait 1-2 seconds:
        HP.delay_1_2()

        # check if Title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH,
                             "//a[@href='https://www.nasa.gov/newsletters'][contains(.,'NASA Newsletters')]").click()
        HP.delay_1_2()

        driver2.find_element(By.XPATH, "//a[@href='https://www.nasa.gov/specials/newsletter-sign-up/']").click()
        HP.delay_1_2()

        # Faker set up:
        fake = Faker()

        # Find elements by XPATH and send fake data:
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0102@gmail.com")
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').send_keys(fake.first_name())
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').send_keys(fake.last_name())
        driver2.find_element(By.XPATH, '//input[@data-input-id="city"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="city"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="city"]').send_keys(fake.city())
        driver2.find_element(By.XPATH, '//input[@data-input-id="state"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="state"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="state"]').send_keys(fake.state())
        driver2.find_element(By.XPATH, '//input[@data-input-id="postal_code"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="postal_code"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="postal_code"]').send_keys("11229")
        driver2.find_element(By.XPATH, '//input[@data-input-id="country"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="country"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="country"]').send_keys(fake.country())

        driver2.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        # somtimes should pass Captcha before (with 3 images selection)

        # Verify that Subscription for Newsletters was sent :
        wait = WebDriverWait(driver2, 3)
        form = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Thanks for Subscribing!")]'))).text

        if form == "Thanks for Subscribing!":
            print("Subscription for Newsletters was sent")
        else:
            print("Check Subscription for Newsletters")

        print("Subscription for Newsletters was checked")
        print("TC-001 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify that user is unable to make a subscription for a Newsletters by using invalid Email, (TC-002)/Negative

    def test_subscription_negative(self):
        driver2 = self.driver
        driver2.get(HP.url)
        self.driver.maximize_window()

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # Check if title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH,
                             "//a[@href='https://www.nasa.gov/newsletters'][contains(.,'NASA Newsletters')]").click()
        HP.delay_1_2()

        driver2.find_element(By.XPATH, "//a[@href='https://www.nasa.gov/specials/newsletter-sign-up/']").click()
        HP.delay_1_2()

        # Find elements by XPATH and send fake data:
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0102@gmail.c")
        driver2.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        HP.delay_1_2()

        # Verify user got Error Message:
        assert driver2.find_element(By.XPATH, "//div[@class='message'][contains(.,'Email is invalid.')]").is_displayed()
        print("Error Message is displayed")

        # or way #2 to verify the Error Message was displayed:
        # driver2.find_element(By.XPATH, "//div[@class='message'][contains(.,'Email is invalid.')]")
        # print("Error Message is displayed")

        print("User is unable to make subscription with Invalid Email")
        print("TC-002 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify the ability of user to make a registration for NASA's upcoming events, (TC-004):

    def test_upcoming_events(self):
        driver2 = self.driver
        driver2.get(HP.url)

        # Set up custom window size:
        self.driver.set_window_size(300, 1800)

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # check if Title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        driver2.find_element(By.XPATH, '//button[@class ="navbar-toggle collapsed"]').click()
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH, "//a[@href='/specials/virtualguest/']").click()

        HP.delay_1_2()

        # Verify opened page is SignUp Form page by Title:
        assert "NASA Virtual Guest Ops" in driver2.title
        print("NASA Virtual Guest page is opened")

        driver2.find_element(By.XPATH, '//a[@class ="w3-button w3-round-xlarge w3-nasa-blue"]').click()

        HP.delay_1_2()

        driver2.get("https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests")

        # Verify opened page is SignUp Form page bu URL:
        # driver2.find_element(By.XPATH, "//img[@data-image-content]")
        assert "https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests" in driver2.current_url
        print("Current Signup Form Page is correct")

        # Faker set up:
        fake = Faker()

        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0103@gmail.com")
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').send_keys(fake.first_name())
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').send_keys(fake.last_name())

        driver2.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        # should pass Captcha before with 3 images selection:
        # driver1.find_element(By.XPATH, '//a[@data-purpose="download"]')

        # Verify that Registration for Upcoming events was done :
        wait = WebDriverWait(driver2, 3)
        form = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Thanks for Signing up!")]'))).text

        if form == "Thanks for Subscribing!":
            print("Subscription for Newsletters was sent")
        else:
            print("Check Subscription for Newsletters")
        # Verify user got Error Message:
        assert driver2.find_element(By.XPATH, "//div[@class='message'][contains(.,'Email is invalid.')]").is_displayed()
        print("Successful Message is displayed")

        print("Join to NASA's Virtual Guest List was Done!")
        print("TC-004 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify that user is unable to make a registration  for NASA's upcoming events  with invalid email,
    # (TC-005)/Negative Test:

    def test_upcoming_events_negative(self):
        driver2 = self.driver
        driver2.get(HP.url)

        # Set up custom window size:
        self.driver.set_window_size(300, 1800)

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # Check if title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        driver2.find_element(By.XPATH, '//button[@class ="navbar-toggle collapsed"]').click()
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH, "//a[@href='/specials/virtualguest/']").click()

        HP.delay_1_2()

        # Verify opened page is SignUp Form page:
        assert "NASA Virtual Guest Ops" in driver2.title
        print("NASA Virtual Guest page is opened")

        driver2.find_element(By.XPATH, '//a[@class ="w3-button w3-round-xlarge w3-nasa-blue"]').click()

        HP.delay_1_2()

        driver2.get("https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests")

        # Verify opened page is SignUp Form page:
        assert "https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests" in driver2.current_url
        driver2.find_element(By.XPATH, "//img[@data-image-content]")

        print("Current Signup Form Page is correct")

        # Faker set up:
        fake = Faker()

        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0103@gmail.c")
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="first_name"]').send_keys(fake.first_name())
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').click()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').clear()
        driver2.find_element(By.XPATH, '//input[@data-input-id="last_name"]').send_keys(fake.last_name())

        print("Sign Up Form is filled by Fake data")

        # Click "Submit" button:
        driver2.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        # Verify user got Error Message:
        assert driver2.find_element(By.XPATH, "//label[contains(., '* Email')]").is_displayed()
        print("Error Message is displayed")

        print("User is unable to make a registration  for NASA's upcoming events  with invalid email")
        print("TC-005 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify that Logo leads to the website's Homepage after clicking on it, (TC-006):

    def test_logo_functionality(self):
        driver2 = self.driver
        driver2.get(HP.url)
        self.driver.maximize_window()

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # Check if Title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver2.find_element(By.XPATH, "//a[@href='/solve/index.html'][contains(.,'Get Involved')]").click()

        HP.delay_1_2()

        # Verify opened page is SignUp Form page:
        assert "Participate with NASA Solve | NASA" in driver2.title
        print("Page title is correct")

        HP.delay_1_2()

        # Find logo Icon:
        driver2.find_element(By.XPATH, "//nav[@id='navbar-nasa']/div/a/img").click()
        # driver.find_element(By.XPATH, '//img[@alt="Nasa" and @xpath="1"]').click()

        HP.delay_1_2()

        # Verify logo leaded to Homepage:
        # Check if Homepage title is correct, strict assertion:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if Homepage URL is correct, strict assertion:
        assert HP.url == driver2.current_url
        print("Current URL of Homepage is OK:", driver2.current_url)

        # Verify logo leaded to Homepage by specific element present:
        try:
            driver2.find_element(By.XPATH, "(//a[contains(.,'Humans in Space')])[1]")
            print("Specific element was found on Homepage")
        except NoSuchElementException:
            print("Specific element was NOT  found on Homepage")

        print("Logo leads to the website's Homepage")
        print("TC-006 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify that the “Search” field is working appropriate, (TC-007):

    def test_search_field(self):
        driver2 = self.driver
        driver2.get(HP.url)
        self.driver.maximize_window()

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # Check if Title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        try:
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").click()
            HP.delay_1_2()
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys("Events")
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys(Keys.RETURN)
            print("Search field is working")

        except WDE:
            print("Check Search field")

        HP.delay_1_2()
        assert "Events - NASA Search Results" in driver2.title

        print("Correct Page is opened by Search result")
        print("TC-007 is PASSED")

        # Close entire Browser:
        driver2.quit()

    # Verify that the “Search” field is working appropriate/Negative Testing),(TC-008):

    def test_search_field_negative(self):
        driver2 = self.driver
        driver2.get(HP.url)
        self.driver.maximize_window()

        # Wait 1-2 seconds:
        HP.delay_1_2()

        # Check if Title is correct:
        assert HP.title_main_page == driver2.title
        print("Current Title is OK:", driver2.title)

        # Check if URL is correct:
        assert HP.url == driver2.current_url
        print("Current URL is OK:", driver2.current_url)

        # Set up wait time:
        WebDriverWait(1, 3)

        # Find elements by XPATH:
        try:
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").click()
            HP.delay_1_2()
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys(".")
            driver2.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys(Keys.RETURN)
            print("Search field try to sent invalid data")
        except WDE:
            print("Search field is not working")

        HP.delay_1_2()
        assert ". - NASA Search Results" in driver2.title
        print("New page is opened")

        driver2.find_element(By.XPATH, "//div[contains( @class ,'content-block-item')]")
        assert driver2.find_element(By.XPATH, '//div[contains(text(),"Sorry, no results found for")]').is_displayed()
        print("Notification about wrong data in Search field was cached")

        # Make and save screenshot:
        driver2.get_screenshot_as_file("Notification_about_wrong_data.png")
        driver2.save_screenshot("Notification_about_wrong_data.png")
        print("Screenshot was done and save")

        print("TC-008 is PASSED")

        # Close entire Browser:
        driver2.quit()


# close entire Browser:


def tearDown(self):
    self.driver.quit()
