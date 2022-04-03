from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime
from fp.fp import FreeProxy
import scrapper
px_list = set()



def start_chrome():
    #PROXY = px
    #options.add_argument('--proxy-server=%s' % PROXY)
    #option = '--proxy-server=' + PROXY
    chrome_options = webdriver.ChromeOptions()
    
    #chrome_options.add_argument('--proxy-server=%s' % PROXY)
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options, executable_path="chromedriver_linux64/chromedriver")
    #driver.set_page_load_timeout(5)
    driver.implicitly_wait(5)
    #visit_site()
    visit_site(driver)



def visit_site(driver):
    #driver.get("https://2ip.ru/")
    #hentai_title = '64524'
    for key, value in drochila_list.items():
        hentai_site = "https://tl.rulate.ru/"
        driver.get(hentai_site)
        time.sleep(1)
        user = driver.find_element_by_name("login[login]")
        user.send_keys(key)
        pas = driver.find_element_by_name("login[pass]")
        pas.send_keys(value)
        pas.submit()
        for hentai_title in hentai_list:
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
            driver.get("https://tl.rulate.ru/book/" + str(hentai_title))
            
            try:
                driver.find_element_by_xpath("//*[@id=\"liker\"]/a").click()
            except:
                print("pizda")
            try:
                driver.get("https://tl.rulate.ru/book/" + str(hentai_title) + "/bm")
            except:
                print("pizda")
            #driver.find_element_by_xpath("//*[@id=\"Info\"]/div[1]/div[2]/div[1]/div/a[5]").click()
            #driver.find_element_by_xpath("//*[@id=\"Info\"]/div[1]/div[2]/div[2]/div/a[5]").click()   
        
        time.sleep(2)

     
    driver.close()  

hentai_list = [
    67129, 
    66362, 
    67747, 
    67701, 
    68304, 
    68315, 
    68253, 
    60863, 
    68262,
    68323, 
    67258, 
    51129, 
    66950, 
    57734, 
    68443,
    67129
        ]

drochila_list = {
    "Mazarella":"2693063az",
    "Mazarella":"2693063az"
}

start_chrome()