
##################################################################################

# Name: flasrefreshpage.py & index19_1.html ,index19_2.html
# Description: Script is used to send servo real time attribute on web page 
# Link: http://192.168.8.225:5000/gmrt   ==> select antenna name and submit 
# Version: 01
# Author: bhavesh kunbi (Telemetry Lab, 8330 , GMRT-NCRA-TIFR)
# Last Modified date: 12 Aug 2021 , New page with flag added servowebpage3.html
##################################################################################
from flask import Flask,render_template, request,json
from flask import Flask, jsonify, render_template, request
import webbrowser
import time
import json
import tango
from tango import DeviceProxy
import csv
from flask import Flask, render_template, request, jsonify
from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from flask import Flask, redirect, url_for, render_template, request
import time
import datetime
import pandas as pd
from datetime import datetime

app = Flask(__name__, template_folder='template')

@app.route("/servo")
def index():
    return render_template("index19_1.html")  

@app.route('/gmrtservo', methods=["GET"])
def gmrtservo():
    dict1={}
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    
    dp= request.args.get('ant')
    dp1 = "tango://"+dp.lower()+":10000/LMC/"+dp.upper()+"/SERVO" #tango://c04:10000/LMC/C04/SERVO   
    device = DeviceProxy(dp1)
    da_list = device.get_attribute_list()
    #print(dp1)
    #print(device)
    #print(da_list)    
    length = len(da_list)   
    #print("total attributes in SERVO system is" ,length)
    
    for i in range(0,length,1):
        data = device[da_list[i]]
        keys = [da_list[i]]
        values = [data.value]
        i=0
        while i < len(keys):
                dict1[keys[i]] = values[i]
                i += 1
        #print(i,da_list[i], "----------------------------",data.value)
    #print(dict1)
    dict1['date'] = date # added date key:value in dict1
    print("sending servo subsystem parametrs......")
    return render_template("servowebpage3.html",dict1=dict1) # web page template designed

if __name__ == '__main__':
    app.run()
    #app.run(host='192.168.8.241', port=5000, debug=True)
