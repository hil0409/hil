from flask import Flask, render_template, request
import pandas as pd
data = pd.read_csv("경기도 양평군_착한가격 음식점.csv", encoding = 'cp949')

app = Flask(__name__)

name = data['업소명']
name.list = name.values.tolist()

price = data['가격']
price.list = price.values.tolist()

location = data['위치']
location.list = location.values.tolist()
print(price.list[0])

@app.route('/')

def hello_world():
    #return render_template("home.html")
    return render_template("html_test.html",  values3 = name.values.tolist(),values = price.list, values2 = location.list)
@app.route('/home.html')
def home():
    return render_template("home.html")
@app.route('/test.html/<Name>')
def info(Name):
    count = 0;
    for n in name.list:
        if Name == n:
            break
        else:
            count += 1
    Price = price.list[count]
    Location = location.list[count]
    return render_template("test.html",name = Name,price = Price,location = Location)
@app.route('/html_test.html')
def list():
    return render_template("html_test.html",  values3 = name.values.tolist(),values = price.list, values2 = location.list)
if __name__ == "__main__":
    app.run(host = 'localhost',port = 8095)
    


