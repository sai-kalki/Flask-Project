from flask import Flask, render_template, request, redirect, url_for,Response
from random import randint,choices,random
import pyodbc
import certifi
ca = certifi.where()

app = Flask(__name__)

# Mongoclient Api
#cluster = MongoClient("mongodb+srv://saiprakash:saiprakash@cluster0.i2gzg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)
#mongodb+srv://saiprakash:saiprakash@cluster0.i2gzg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority


app.secret_key =  "b'_5#y2LF4Q8z\n\6746c]/'"


"""
conn = pyodbc.connect("Driver = {SQL Server};"
                      "Server = tcp: swebapp.database.windows.net, 1433;"
                      "Database = userdetails;"
                      "Uid = sara;"
                      "Pwd = Asdf1234;"
                      "Encrypt = yes;"
                      "TrustServerCertificate = no;"
                      "Connection Timeout = 30;")

"""



@app.route("/",methods=["POST","GET"])
@app.route("/index",methods=["POST","GET"])
def index():
    if request.method=="POST":
        form = dict(request.form)
        first_name = form["first_name"]
        surname = form["surname"]
        email = form["Email"]
        contact = form["Contact"]
        github = form["url"]

        #Uncomment if below code works
        """
        try:
            curs = conn.cursor()
            curs.execute(f"insert into basicdetails values({first_name},{surname},{email},{contact},{github})")
        except Exception as err:
            raise err
        """

        return redirect(url_for("search"))
    else:
        return render_template("index.html")


@app.route("/search",methods=["POST","GET"])
def search():
    if request.method=="POST":
        contact = (request.form)["contact"]

        # delete below dict if code worked, Just for demo
        details = {
            "firstname":"Saiprakash",
            "surname":"Ajithkumar",
            "email":"ssasai007@gmail.com",
            "contact":8637483834,
            "github":"https://github.com/sai-kalki"
        }

        #Uncomment this if below code works
        """
        try:
            curs = conn.cursor()
            details = curs.execute(f"select * from basicdetails where contact='{contact}'")
            return render_template("search.html",posted=True,noResult=True,firstname=details['firstname'],surname=details['surname'],email=details['email'],contact=details['contact'],github=details['github'])
        except Exception as err:
            return render_template("search.html",posted=True,noResult=False,firstname="",surname="",email="",contact="",github="")
            raise err
        """
        
        return render_template("search.html",posted=True,firstname=details['firstname'],surname=details['surname'],email=details['email'],contact=details['contact'],github=details['github'])
    else:
        return render_template("search.html",posted=False,noResult=False,firstname="",surname="",email="",contact="",github="")




if __name__ == "__main__":
    app.run(debug=True)




