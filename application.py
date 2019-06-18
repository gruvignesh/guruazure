# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

from flask import Flask, render_template
import pypyodbc
app = Flask(__name__)
connection = pypyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:gurucloud.database.windows.net,1433;Database=gurudb;Uid=gurucloud;Pwd=Guruearthquake1;")

@app.route('/')
def hello_world():
    cursor = connection.cursor()
    cursor.execute("select count(*) from all_month")
    rows = cursor.fetchall()
    count = rows[0][0]
    return render_template('index.html', count=count)


if __name__ == '__main__':
    app.run()