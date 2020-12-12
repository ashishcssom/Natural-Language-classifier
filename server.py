#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask,request
import pandas as pd
import json
import src
app = Flask(__name__)
 
@app.route('/Request', methods = ['POST','GET'])
def RequestHandler():
    """ method to predict commitment """
    content = request.get_json()
    Data=pd.DataFrame([content])
    try:
        output=src.main(Data,filename="Request")
    except:
        output=[]
    return(output)

if __name__=="__main__":
    app.run(debug=True)
