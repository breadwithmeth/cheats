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
    #hentai_title = '64524'
    hentai_site = "https://tl.rulate.ru/book/" + hentai_title
    #hentai_site = 'https://2ip.ru/'
    driver.get(hentai_site)
    assert " " in driver.title
    elem = driver.find_element_by_link_text('Начать чтение')
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    assert "No results found." not in driver.page_source
    driver.close()  

def start_chrome(px):
    PROXY = px
    #options.add_argument('--proxy-server=%s' % PROXY)
    #option = '--proxy-server=' + PROXY
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(options=chrome_options, executable_path="chromedriver_linux64/chromedriver")
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
hentai_title = str(input("Title ID: "))
while True:
    px_list = scrap_proxy()
    i = 0
    for ip in px_list:
        if timer(ending):
            break
        px = ip
        if check_proxy(px):
            print('-'+px+' is alive. ({} left)'.format(str(len(px_list))))
            try:
                start_chrome(px)
            except:
                print('NEGATIVE')
    if timer(ending):
            break
        