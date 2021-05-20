from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

import time
PROXY = "51.222.21.92:32769" # IP:PORT or HOST:PORT initial port to collect proxy

class Checkingoutaproxy:

    def __init__(self):
        # using selenium to find the ips
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
        self.chrome = webdriver.Chrome(chrome_options=chrome_options)
        self.chrome.maximize_window()
        self.chrome.get('https://free-proxy-list.net/')
        self.chrome.maximize_window()
        m=[]
        getMaxShow = self.chrome.find_element(By.CLASS_NAME,'dataTables_length').click()
        clickMaxShow = self.chrome.find_element(By.XPATH,'//*[@id="proxylisttable_length"]/label/select/option[3]').click()
        gettingIPTable = self.chrome.find_element(By.CLASS_NAME,'dataTable')
        gettingRow = gettingIPTable.find_element(By.TAG_NAME,'tbody')
        gettingColumn = gettingRow.find_elements(By.CSS_SELECTOR,'[role="row"] td:nth-child(1)')
        gettingColumn2 = gettingRow.find_elements(By.CSS_SELECTOR,'[role="row"] td:nth-child(2)')
        print(len(gettingColumn))
        print(type(gettingColumn))

        i=0

        # storing ips in a list
        for ip in gettingColumn:
            if i<len(gettingColumn):
                m.append(ip.text + ":" + gettingColumn2[i + 1].text)
            else:
                break
        print(*m,sep = "\n")
        time.sleep(3)
        self.connectWithNewIP(m)

    # method for checking the validity of the collected ips
    def connectWithNewIP(self,ips):
        for ip in ips:
            print("checking IP"+ip)
            e.say("checking IP"+ip)
            e.runAndWait()
            try:
                authProxy = requests.get('https://httpbin.org/ip', proxies={'http': ip, 'https': ip})
                print(authProxy.json(), '--> working')
                print("stoping here")
                break
            except Exception:
                pass
        print('Success ip:'+ip)
        self.openWebsiteWithProxy(ip)
        self.chrome.quit()

    # connecting the website with the new ip
    def openWebsiteWithProxy(self,ip):

        try:
            webdriver.DesiredCapabilities.CHROME['proxy'] = {
                "httpProxy": ip,
                "ftpProxy": ip,
                "sslProxy": ip,
                "proxyType": "MANUAL",

            }

            webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
            self.chrome.get('https://whatismyipaddress.com/')
        except Exception:
            pass

test = Checkingoutaproxy()
