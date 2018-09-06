from bs4 import BeautifulSoup
import urllib3
from googlesearch import search as sr
from datetime import datetime as dt
import re
import time
import csv
import config as cf


def search(city,date):
    l=[]
    try:
        query="weather.com " + city
        for j in sr(query, tld="com", num=1, stop=1, pause=0):
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
        if city in cf.ct:
            l.append(round(float(q2[2]),2))
            l.append(round(float(k.split('Wind')[len(k.split('Wind')) - 1].split(' ')[1]),5))
            l.append(round(float(k.split('Wind')[len(k.split('Wind')) - 1].split('Visibility')[1].split(' ')[0]),2))
        else:
            l.append(round(((float(q2[2])-32.0)*(5.0/9)),2))
            l.append(round(1.6*float(k.split('Wind')[len(k.split('Wind')) - 1].split(' ')[1]),2))
            l.append(round(1.6*float(k.split('Wind')[len(k.split('Wind')) - 1].split('Visibility')[1].split(' ')[0]),2))
        l.append(k.split('Wind')[len(k.split('Wind'))-1].split(' ')[0])
        l.append(k.split(u'\N{DEGREE SIGN}')[1].split("Feels")[0])
        try:
            with open(cf.path + city + "_" + date + '.csv', 'r') as k:
                k.close()
        except:
            with open(cf.path + city + "_" + date + '.csv', 'w') as k:
                csv.writer(k).writerow(cf.v)
                k.close()
        with open(cf.path + city + "_" + date + '.csv', 'a') as f:
            csv.writer(f).writerow(l)
            f.close()
        return l
    except:
        print "Not working! Check internet connection"
        exit()


if __name__=='__main__':
    start_time = time.time()
    print search("Chennai","2018-09-05")
    print "Time taken to execute: " + str(time.time() - start_time) + " seconds"