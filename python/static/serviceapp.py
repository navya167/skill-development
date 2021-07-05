import re
from flask import Flask,render_template,request
import sys
app = Flask(__name__)

@app.route('/')
def loadform():
    print(sys.version)
    return render_template('index.html')


@app.route('/result',methods = ['POST','GET'])
def result():
   data =  request.args.get('data')
   import calculator
   result = calculator.calculate(data)
   print('result',result,type(result))
   if type(result) == str:
       return {'result':result},400
   else:
       return {'result':result},200
    


if __name__ == "__main__":
    app.run()

