import time
import pandas as pd
from bs4 import BeautifulSoup
from requests import session

class Stocks():
    def __init__(self,url,company) -> None:
        self.url = url
        self.company = company
        self.Open = None
        self.Previous_Close = None
        self.High = None
        self.Low = None
        self.UC_Limit = None
        self.LC_Limit = None
        self.ltp = None
        self.session = session()

    def getData(self):
        while True:
            response = self.session.get(self.url)
            if response.status_code == 200:        
                html = response.content
                soup = BeautifulSoup(response.text, 'html.parser')
                self.ltp = float(soup.find(id="nsecp")['rel'])

                df_list = pd.read_html(html)
                t1 = df_list[2]
                t2 = df_list[3]

                allValues_T1 = t1.values[:]
                allValues_T2 = t2.values[:]

                self.Open = float(allValues_T1[0][1])
                self.Previous_Close = float(allValues_T1[1][1])

                self.High = float(allValues_T2[0][1])
                self.Low = float(allValues_T2[1][1])
                self.UC_Limit = float(allValues_T2[2][1])
                self.LC_Limit = float(allValues_T2[3][1])

                if (self.ltp > (self.Previous_Close + 50)) or (self.ltp < (self.Previous_Close - 50)):
                    print("ALERT: " + self.company + " = " + str(self.ltp) + " (" + str(round(self.ltp - self.Previous_Close,2)) + ")")
                    time.sleep(0.5)
                    continue
                else:
                    print('NOT ALERT:',self.company)
                    time.sleep(0.5)
                    continue
            else:
                print(response.status_code)
                print(response.text)
                exit()
