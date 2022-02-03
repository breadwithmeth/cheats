from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
px_list = set()


def get_html():
    site = 'https://www.sslproxies.org/'
    r = requests.get(site)
    return r.text

def scrap_proxy():  
    global px_list
    px_list = set()
    soup = BeautifulSoup(get_html(), 'lxml')
    line = soup.find('table').find('tbody').find_all('tr')

    for tr in line:
        td = tr.find_all('td')
        ip = td[0].text
        port = td[1].text
        
        px_list.add(':'.join([ip, port]))

    print("---New proxy scraped, left: " + str(len(px_list)))
    return px_list



def check_proxy(px):
    try:
        requests.get("https://tl.rulate.ru/book/28585", proxies = {"http": "http://" + px}, timeout = 2)
    except Exception as x:
        print('--'+px + ' is dead: '+ x.__class__.__name__)
        return False
    return True

"""
def get_proxy():
    px_list = scrap_proxy()
    for ip in px_list:
            px = ip
            if check_proxy(px):
                print('-'+px+' is alive. ({} left)'.format(str(len(px_list))))
                break
    
    return px

"""

def visit_site(driver):
    #driver.get("https://2ip.ru/")
    #hentai_title = '64524'
    for hentai_title in hentai_list:
        #driver.get("https://2ip.ru/")

        hentai_title = str(hentai_title)
        #driver.execute_script("window.open('about:blank', {hentai_title});")
        #driver.switch_to.window("{hentai_title}}")
        try:
            hentai_site = "https://tl.rulate.ru/book/" + hentai_title
            driver.get(hentai_site)
            time.sleep(0)
        except:
            exit
    driver.close()  

def start_chrome(px):
    PROXY = px
    #options.add_argument('--proxy-server=%s' % PROXY)
    #option = '--proxy-server=' + PROXY
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options, executable_path="chromedriver_linux64/chromedriver")
    driver.set_page_load_timeout(3)
    driver.implicitly_wait(3)
    #visit_site()
    try:
        visit_site(driver)
    except:
        print('NEGATIVE')


def timer(ending):
    times = time.perf_counter()
    if times > ending:
        return True
    else:
        return False


"""
while True:
    PROXY = get_proxy()
    #options.add_argument('--proxy-server=%s' % PROXY)
    #option = '--proxy-server=' + PROXY
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=os.path.abspath("chromedriver_linux64/chromedriver"))
    #visit_site()
    try:
        visit_site()
    except:
        print('NEGATIVE')
        """



minutes = int(input("minutes: "))
begining = time.perf_counter()
secs = minutes * 60
ending = secs + begining
#hentai_title = str(input("Title ID: "))

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
    67129, 
    66362, 
    67747, 
    67701, 
    68304, 
        ]
while True:
    px_list = scrap_proxy()
    i = 0
    for ip in px_list:
        if timer(ending):
            break
        px = ip
        if check_proxy(px):
            print('-'+px+' is alive. ({} left)'.format(str(len(px_list))))
            start_chrome(px)
    if timer(ending):
            break
        