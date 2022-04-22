from pickle import TRUE
from flask import Flask,render_template,request
import IR_model as m


app=Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sub",methods=['POST'])
def submit():
    if request.method=="POST":
        city=request.form["city"]
        query=request.form["query"]
        df=m.initialProcess()
        print(df)

    return render_template("sub.html",Ucity=city,Uquery=query)

    

if __name__=="__main__":
    app.run(debug=True)