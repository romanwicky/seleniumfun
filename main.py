from selenium import webdriver
import time

# Chrome
browser = webdriver.Chrome("C:/Users/rwick/PycharmProjects/seleniumtesting/chromedriver.exe")

#Random page
browser.get("https://www.bestbuy.com/site/apple-watch-series-6-gps-44mm-space-gray-aluminum-case-with-black-sport-band-space-gray/6215931.p?skuId=6215931")

buyButton = False

while not buyButton:

    try:

        addtoCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")

        print("Button isn't ready")
        time.sleep(1)
        browser.refresh()

    except:

        addtoCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

        print("Button Clicked")
        addtoCartBtn.click()
        buyButton = True


