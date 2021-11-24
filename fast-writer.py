from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://10fastfingers.com/typing-test/english")

time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/button[4]').click()


input_box = driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[8]/div[2]/div/div[1]/input')


while True:
    try:
        text = driver.find_element_by_xpath(f'/html/body/div[5]/div/div[4]/div/div[1]/div[8]/div[1]/div/span[1]')
        break
    except:
        time.sleep(0.1)



h=1
while True:
    try:
        text = driver.find_element_by_xpath(f'/html/body/div[5]/div/div[4]/div/div[1]/div[8]/div[1]/div/span[{h}]').text
    except:
        print("Done")
        break
    print(text)
    input_box.send_keys(text + Keys.SPACE)
    h+=1
