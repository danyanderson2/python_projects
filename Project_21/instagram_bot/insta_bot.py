from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaBot:
    def __init__(self):
        self.driver=webdriver.Chrome(options=chrome_options,executable_path=r'D:\Python Extra\webdrivers\chrome\chromedriver.exe')
    def connect_to_instagram(self,username,password):
        time.sleep(3)
        self.driver.get('https://instagram.com')
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(15)
        self.driver.find_element(by=By.XPATH,value="//div[contains(text(),'Not now')]").click()
        self.driver.find_element(by=By.XPATH,value="//button[contains(text(),'Not Now')]").click()
    def follow_account(self,account):
        self.driver.get(f"https://www.instagram.com/{account}/")
        time.sleep(10)
        self.driver.find_element_by_xpath("//div[contains(text(),'Follow')]").click()
    def find_follower(self,target):

        self.driver.get(f"https://www.instagram.com/{target}/followers")
        time.sleep(5)
        # # # #Getting hold the popup element and scrolling to bottom
        element=self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",element)
        time.sleep(2)
            # execute_script enables execution of some javascript it can also accept HTML elements
            # The first element within the popup will occupy argument[0] in the script
            # the script will then scroll the followers(elements in the popup) by the height of the popup

    #     #selecting all the buttons 'follow' buttons
    def follow(self):
        time.sleep(10)
        buttons=self.driver.find_elements_by_xpath("//div[contains(text(),'Follow')]")
        time.sleep(2)
        for button in buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                # self.driver.find_element_by_xpath('//button[contains(text(),"cancel")]')
                pass


