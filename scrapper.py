from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
def parse():
    
    y= datetime.today().strftime('%Y')
    m= datetime.today().strftime('%m')
    d= datetime.today().strftime('%d')
    if d == '1':
        m = int(m) - 1
        m = str(m)
    else:
        d = int(d) - 1
        d = str(d) 
    my_file = open("px" + ".txt", "w")
    driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver')
    id = y + "-" + m + "-" + d 
    url = 'https://checkerproxy.net/archive/' + str(id)
    driver.get(url)

    time.sleep(10)
    table = driver.find_element(By.ID, "resultTable")
    soup = BeautifulSoup(driver.page_source, 'lxml')
    line = soup.find('table').find('tbody').find_all('tr')
    for tr in line:
            td = tr.find_all('td')
            ip = td[0].text
            type = td[2].text
            if type == "HTTPS" or type == "HTTP":
                #print(type)
                my_file.write(ip + "\n")
    driver.close ()


