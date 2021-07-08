import re
from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin
import sys

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
@cross_origin(supports_credentials=True)
def loadform():
    print(sys.version)
    return render_template('index.html')


@app.route('/result',methods = ['POST','GET'])
@cross_origin(supports_credentials=True)
def result():
   data =  request.args.get('data')
#    import calculator
   from app.calculator import calculate
   result = calculate(data)
   print('result',result,type(result))
   if type(result) == str:
       return {'result':result},400
   else:
       return {'result':result},200
    



