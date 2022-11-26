from flask import Flask,request,render_template,jsonify
import config
from project.utils import Insurance
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] ="root"
app.config["MYSQL_PASSWORD"] = "Shilpa291994"
app.config["MYSQL_DB"] = "db_travel"
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/INSURE", methods = ["GET","POST"])
def pred_insurance():
    data = request.form
    Age  = int(data["Age"])
    GraduateOrNot = data["GraduateOrNot"]
    AnnualIncome = eval(data["AnnualIncome"])
    FamilyMembers = int(data["FamilyMembers"])
    ChronicDiseases = int(data["ChronicDiseases"])
    FrequentFlyer = data["FrequentFlyer"]
    EverTravelledAbroad = data["EverTravelledAbroad"]
    GovernmentSector = data["GovernmentSector"]
    INS = Insurance(Age,GraduateOrNot,AnnualIncome,FamilyMembers,ChronicDiseases,FrequentFlyer,EverTravelledAbroad,GovernmentSector)
    result = INS.get_insure()

    cursor = mysql.connection.cursor()
    query =  "CREATE TABLE IF NOT EXISTS Travel(AGE VARCHAR(20),GRADUATEORNOT VARCHAR(20),ANNULINCOME VARCHAR(20),FAMILYMEMBERS VARCHAR(20),CHRONICDISEASES VARCHAR(20),FREQUENTFLYER VARCHAR(20),EVERTRAVELLEDABROAD VARCHAR(25),GOVERMENTSECTOR VARCHAR(20),INSURANCE VARCHAR(20))"
    cursor.execute(query)
    cursor.execute("INSERT INTO Travel(AGE,GRADUATEORNOT,ANNULINCOME,FAMILYMEMBERS,CHRONICDISEASES,FREQUENTFLYER,EVERTRAVELLEDABROAD,GOVERMENTSECTOR,INSURANCE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Age,GraduateOrNot,AnnualIncome,FamilyMembers,ChronicDiseases,FrequentFlyer,EverTravelledAbroad,GovernmentSector,result))

    mysql.connection.commit()
    cursor.close()

    return render_template("index1.html",result = result)

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = config.PORT_NUMBER)