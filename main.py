import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import sys
from time import sleep
import message
import os


def check():
    # url = "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=181415"
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.get(url)
    while True:
        cc_url = "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=181415"
        ne_url = 'https://www.newegg.ca/asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p/N82E16814126452?Description' \
                 '=3080%20tuf&cm_re=3080_tuf-_-14-126-452-_-Product '
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(cc_url)
        stock = driver.find_element_by_xpath('//*[@id="pi-form"]/div[2]/div[1]/span[1]')
        store = driver.find_element_by_xpath('//*[@id="pi-form"]/div[2]/div[1]/span[2]')
        # print('message:')
        # print(stock.text)
        # this stock check for canada computers just works
        if 'Not Available' in stock.text:
            print(stock.text)
        else:
            message.send_sms("TUF Online: https://www.canadacomputers.com/product_info.php?cPath=43_557_559"
                             "&item_id=181415")
            return True
        if 'Out Of Stock' in store.text:
            print(store.text)
        else:
            message.send_sms("TUF In Store: https://www.canadacomputers.com/product_info.php?cPath=43_557_559"
                             "&item_id=181415")
            return True
        driver.get(ne_url)
        stock = driver.find_element_by_class_name('product-inventory')
        if 'OUT OF' in stock.text:
            print(stock.text)
        else:
            message.send_sms("Newegg: " + ne_url)
            return True
        driver.quit()
        print(datetime.datetime.now())
        if datetime.datetime.now().hour > 20 or datetime.datetime.now().hour < 8:
            print("good night")
            # os.system('clear')
            sleep(1800)
        sleep(120)

# def check_newegg():
#     url = 'https://www.newegg.ca/asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p/N82E16814126452?Description=3080' \
#           '%20tuf&cm_re=3080_tuf-_-14-126-452-_-Product '
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get(url)
#     stock = driver.find_element_by_class_name('product-inventory')
#     print(stock.text)


if __name__ == '__main__':
    if 'test' in sys.argv:
        message.send_sms("Tuf test: https://www.canadacomputers.com/product_info.php?cPath=43_557_559"
                         "&item_id=181415")
    else:
        check()
