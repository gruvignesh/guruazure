# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

from flask import Flask, render_template
import pypyodbc
app = Flask(__name__)
connection = pypyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:gurucloud.database.windows.net,1433;Database=gurudb;Uid=gurucloud;Pwd=Guruearthquake1;")

@app.route('/')
def hello_world():
    cursor = connection.cursor()
    cursor.execute("select count(*) from all_month")
    rows = cursor.fetchall()
    count = rows[0][0]
    return render_template('index.html', count=count)

@app.route('/query_random', methods=['GET', 'POST'])
def query_random():
	cursor=connection.cursor()
	query_limit = request.args['query_limit']
	start_time = time.time()
	list_of_times = []
	for i in range(0, int(query_limit)):
		start_intermediate_time = time.time()
		select = '''select * from quakes order by rand() limit 1 '''
		#stmt = ibm_db.prepare(db, select)
		cursor.execute(select)
		end_intermediate_time = time.time()
		intermediate_time = end_intermediate_time - start_intermediate_time
		list_of_times.append(intermediate_time)
	end_time = time.time()
	time_taken = (end_time - start_time) / int(query_limit)
	return render_template('graph.html', time_taken=time_taken, list_of_times=list_of_times)



if __name__ == '__main__':
    app.run()