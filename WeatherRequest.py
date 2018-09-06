#unicode(u'\N{DEGREE SIGN}C')
import csv
from bs4 import BeautifulSoup
import urllib3
from googlesearch import search
from datetime import datetime as dt
import time
import re
import datetime
import config as cf

class RequestWeather:
    def __init__(self):
        self.city="Pune"
        self.date=str(datetime.date.today())
    def search(self):
        l=[]
        try:
           query="weather.com " + self.city
           for j in search(query, tld="com", num=1, stop=1, pause=0):
               s = j
           URL = str(s)
           print(URL)
           http = urllib3.PoolManager()
           r = http.request('GET', URL)
           soup = BeautifulSoup(r.data, 'html5lib')
           soup.prettify()
           content = soup.find("div", {"class": "today_nowcard"})
           k=unicode(content.text)
           q=re.findall(r'[\w\.{2}]+:[\w\.{2}]+',k)
           q1=re.findall(r'[\w\.{2}]+:[\w\.{2}]+ [\w]+m',k)
           q2=re.findall(r'[\d{2}]+',k)
           if q1:
               in_time = dt.strptime(q1[0], "%I:%M %p")
               out_time = dt.strftime(in_time, "%H:%M")
               l.append(out_time)
           else:
               l.append(q[0])
           if self.city in cf.ct:
               l.append(q2[2])
           else:
               l.append((float(q2[2])-32.0)*(5.0/9))
           l.append(k.split(u'\N{DEGREE SIGN}')[1].split("Feels")[0])
           try:
               with open(cf.path+self.city+"_"+self.date+'.csv', 'r') as k:
                   k.close()
           except:
               with open(cf.path+self.city+"_"+self.date+'.csv', 'w') as k:
                    csv.writer(k).writerow(cf.v)
                    k.close()
           with open(cf.path+self.city+"_"+self.date+'.csv', 'a') as f:
               csv.writer(f).writerow(l)
               f.close()
        except:
            print "Not Working! Check internet connection"
            exit()



if __name__=='__main__':
    start_time=time.time()
    a=RequestWeather()
    a.city="Chennai"
    a.search()
    print "Time taken to execute: "+ str(time.time()-start_time) + " seconds"