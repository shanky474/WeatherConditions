from flask import Flask, render_template, request
import Analysis as anl
import RTAnalysis as rt
import time
import config as cf
import datetime
import itertools

app=Flask(__name__)


@app.route('/')
def WeatherGUI():
   return render_template('WeatherGUI.html')

@app.route('/getdetails', methods = ['POST'])
def details():
     cf.city=request.form['cities']
     cf.date=request.form['date']
     if str(cf.date) == str(datetime.date.today()):
        try:
           while True:
                k=rt.search(cf.city,cf.date)
                tempval = float(k[1])
                direction=k[4]
                visibility=k[3]
                wind=k[2]
                sky=k[5]
                color="red" if tempval > 40 else "black"
                return render_template('TestRT1.html', tempval=tempval, color=color, angle=cf.wind[direction], visibility=visibility, wind=wind, sky=sky)
        except:
                print("Troubleshooting needed!")
     else:
         anl.data(cf.city,cf.date).plots()
         return render_template('AnalysisGUI.html',path=cf.city+"_"+cf.date+'.jpg')


@app.route('/TestRT2', methods=['GET', 'POST'])
def DisastersGUI1():
    try:
        while True:
            k = rt.search(cf.city, cf.date)
            tempval = float(k[1])
            direction = k[4]
            visibility = k[3]
            wind = k[2]
            sky = k[5]
            color = "red" if tempval > 40 else "black"
            return render_template('TestRT2.html', tempval=tempval, color=color, angle=cf.wind[direction],
                                   visibility=visibility, wind=wind, sky=sky)
    except:
        print("Troubleshooting needed!")


@app.route('/TestRT1', methods=['GET', 'POST'])
def DisastersGUI2():
    try:
        while True:
            k = rt.search(cf.city, cf.date)
            tempval = float(k[1])
            direction = k[4]
            visibility = k[3]
            wind = k[2]
            sky = k[5]
            color = "red" if tempval > 40 else "black"
            return render_template('TestRT1.html', tempval=tempval, color=color, angle=cf.wind[direction],
                                   visibility=visibility, wind=wind, sky=sky)
    except:
        print("Troubleshooting needed!")


@app.route('/goback', methods=['GET', 'POST'])
def RealTimeGUI():
    return render_template('WeatherGUI.html')


@app.route('/DisastersGUI')
def DisastersGUI():
    return render_template('DisastersGUI.html')

@app.route('/AboutGUI')
def AboutGUI():
   return render_template('AboutGUI.html')

if __name__=='__main__':
    app.run(threaded=True)
