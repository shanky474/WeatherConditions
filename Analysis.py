import pandas as pd
import config as cf
from matplotlib import pyplot as plt
import datetime
import numpy as np
import time


class data:
    def __init__(self,city,date):
        self.city = city
        self.date = date
        self.df = pd.read_csv(cf.path+self.city+"_"+self.date+'.csv')
        self.x = np.array([v for v in range(len(self.df))])
    def plots(self):
        plt.figure(figsize=(17, 8))
        plt.subplot(1,3,1)
        plt.title("Wind Speed plot")
        plt.xticks(self.x,self.df[cf.v[0]],rotation=90)
        plt.grid()
        plt.xlabel("Time")
        plt.ylabel("Wind Speed in "+u'Km/h')
        plt.plot(self.x,self.df[cf.v[2]],marker='o')
        plt.subplot(1,3,2)
        plt.title("Temperature bar graph")
        plt.grid()
        plt.ylabel("No. of times")
        plt.xlabel("Temperature in " + u'\N{DEGREE SIGN}C')
        plt.hist(self.df[cf.v[1]],bins=50)
        plt.subplot(1,3,3)
        plt.title("Visibility plot")
        plt.xticks(self.x,self.df[cf.v[5]], rotation=90)
        plt.grid()
        plt.ylabel("Visibility in Km")
        plt.xlabel("Sky Conditions")
        plt.violinplot(self.df[cf.v[3]])
        plt.savefig(cf.pathfig+self.city+"_"+self.date+'.jpg')



if __name__=='__main__':
    start_time = time.time()
    data("Hyderabad","2018-09-01").plots()
    print "Time taken to execute: " + str(time.time() - start_time) + " seconds"