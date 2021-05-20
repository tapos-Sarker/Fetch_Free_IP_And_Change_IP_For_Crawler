from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pyttsx3
import requests

e = pyttsx3.init()
voices = e.getProperty('voices')
e.setProperty('voice', voices[1].id)
rate = e.getProperty('rate')
e.setProperty('rate', rate-50)
import time
PROXY = "51.222.21.92:32769" # IP:PORT or HOST:PORT

class Checkingoutaproxy:

    def __init__(self):

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
        # print(*map(str,gettingColumn), sep = "\n")
        i=0
        for ip in gettingColumn:
            if i<len(gettingColumn):
                m.append(ip.text + ":" + gettingColumn2[i + 1].text)
            else:
                break
        print(*m,sep = "\n")
        time.sleep(3)
        self.connectWithNewIP(m)


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
            # try:
            #     # time.sleep(3)
            #     print("checking > "+ip)
            #     try:
            #
            #         # exit()
            #     except Exception:
            #         pass
            # except Exception:
            #     # self.chrome.quit()
            #     pass

        print('new ip:'+ip)
        self.openWebsiteWithProxy(ip)
        self.chrome.quit()


    def openWebsiteWithProxy(self,ip):
        e.say("I'm here")
        e.runAndWait()
        # try:
        #     chrome_options = webdriver.ChromeOptions()
        #     chrome_options.add_argument('--proxy-server=http://%s' % format(ip))
        #     self.chrome = webdriver.Chrome(chrome_options=chrome_options)
        #     self.chrome.maximize_window()
        #     l = self.chrome.get('https://www.whatismyip.com/')
        #     l = self.chrome.get('https://httpbin.org/ip')
        #     print(l.json())
        try:
            webdriver.DesiredCapabilities.CHROME['proxy'] = {
                "httpProxy": ip,
                "ftpProxy": ip,
                "sslProxy": ip,
                "proxyType": "MANUAL",

            }

            webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
            # self.chrome.get('https://www.whatismyip.com/')
            # self.chrome.quit()
            self.chrome.get('https://whatismyipaddress.com/')
        except Exception:
            # self.connectWithNewIP(self.m)
        # self.chrome.maximize_window()
            pass
test = Checkingoutaproxy()


# chrome.get("http://whatismyipaddress.com")