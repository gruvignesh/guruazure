# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

from flask import Flask, render_template,request
import random
import pypyodbc
#import random
import time
import json
#import pygal
# import random
#import redis
app = Flask(__name__)
connection = pypyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:gurucloud.database.windows.net,1433;Database=gurudb;Uid=gurucloud;Pwd=Guruearthquake1;")

@app.route('/')
def hello_world():
    cursor = connection.cursor()
    cursor.execute("select count(*) from quake6")
    rows = cursor.fetchall()
    count = rows[0][0]
    return render_template('index.html', count=count)
# @app.route('/')
# def hello_world():
#     return render_template('common.html', )


@app.route('/question1', )
def question1():
    return render_template('question1.html')

# @app.route('/question1_execute', methods=['GET'])
# def question1_execute():
#     bar_chart = pygal.Bar(width=1000, height=500)
#     sql = "select TOP 5 latitude,depth from quake6"
#     # print(sql)
#     cursor = conn.cursor()
#     result = cursor.execute(sql).fetchall()
#     population_values = []
#     state = []
#     for r in result:
#         state.append(str(r[0]))
#         population_values.append(r[1])
#         # state = r[0]
#         # population_values = []
#         bar_chart.add(state, population_values)
#     return render_template('question1.html', chart=bar_chart.render_data_uri())

@app.route('/charting')
def charting():
    # cursor = connection.cursor()
    # cursor.execute("select count(*) from quake6")
    # rows = cursor.fetchall()
    # count = rows[0][0]
    return render_template('index.html', count=count)



@app.route('/query_random', methods=['GET', 'POST'])
def query_random():
	cursor=connection.cursor()
	query_limit = request.args['query_limit']
	start_time = time.time()
	list_of_times = []
	for i in range(0, int(query_limit)):
		start_intermediate_time = time.time()
		#select = '''select * from quakes order by rand() limit 1 '''
		#stmt = ibm_db.prepare(db, select)
		cursor.execute("select TOP 1 * from all_month order by rand()")
		end_intermediate_time = time.time()
		intermediate_time = end_intermediate_time - start_intermediate_time
		list_of_times.append(intermediate_time)
	end_time = time.time()
	time_taken = (end_time - start_time) / int(query_limit)
	#time_taken=89
	#list_of_times=[10,20,30]
	return render_template('graph.html', time_taken=time_taken, list_of_times=list_of_times)

# @app.route('/restricted')
# def restricted():
# 	cursor=connection.cursor()
# 	host_name='gururedis.redis.cache.windows.net'
# 	password='FmVTs5VAIAUQ4Ly84bYkTcNC9FXWIShAIqGXQSALvfM='
# 	cache = redis.StrictRedis(host=host_name, port=6380, password=password, ssl=True)
# 	query_limit = request.args['query_limit1']
# 	lowmag = request.args['lowmag']
# 	highermag = request.args['highermag']
# 	start_time1 = time.time()
# 	list_of_times = []
# 	range_pairs=[]
# 	for i in range(0, int(query_limit)):
# 		rang=[]
# 		start_intermediate_time = time.time()
# 		rngvalue1 = random.uniform(float(lowmag), float(highermag))
# 		rngvalue2 = random.uniform(float(lowmag), float(highermag))
# 		rang.append(rngvalue1)
# 		rang.append(rngvalue2)
# 		if not cache.get(rngvalue1):
# 			if not cache.get(rngvalue2):
# 				sql='select count(*) from quake6 where depthError between ? AND ?'
# 				rows = cursor.fetchall()
# 				cache.set(magnitude, str(rows))
# 		else:
# 			rows_string = cache.get(magnitude)
# 		end_intermediate_time = time.time()
# 		intermediate_time = end_intermediate_time - start_intermediate_time
# 		list_of_times.append(intermediate_time)
# 		range_pairs.append(rang)
# 	end_time1 = time.time()
# 	time_taken = (end_time1 - start_time1) / int(query_limit)
# 	#return render_template('restricted.html',time_taken=time_taken)
# 	return render_template('restricted.html',time_taken=time_taken,list_of_times=list_of_times,range_pairs=range_pairs)

@app.route('/question5')
def question5():
	cursor=connection.cursor()
	#query_limit = request.args['query_limit1']
	lowmag = request.args['lowdep']
	highermag = request.args['higherdep']
	longitude=request.args['Longitude']
	sql='select time,latitude,longitude,depthError from quake6 where (depthError between ? AND ?) AND longitude>? '
	cursor.execute(sql, (lowmag,highermag,longitude))
	rows = cursor.fetchall()
	#start_time1 = time.time()
	# for i in range(0, int(query_limit)):
	# 	rngvalue = random.uniform(float(lowmag), float(highermag))
	# 	sql = 'select * from all_month where mag>=? '
	# 	cursor.execute(sql, (rngvalue,))
	#end_time1 = time.time()
	#time_taken = (end_time1 - start_time1) / int(query_limit)
	#return render_template('restricted.html',time_taken=time_taken)
	return render_template('output.html',rows=rows)


@app.route('/chartcheck', methods=['GET', 'POST'])
def chartcheck():
	cursor=connection.cursor()
	query_limit = request.args['chart1']
	sql='select TOP 5 latitude,depthError from quake6'
	cursor.execute(sql)
	rows = cursor.fetchall()
	xaxis=[]
	yaxis=[]
	for r in rows:
		xaxis.append(r[0])
		yaxis.append(r[1])

	#xaxis=['g', 'o', 'm']
	#yaxis=[20, 14, 23]
	# start_time = time.time()
	# list_of_times = []
	# for i in range(0, int(query_limit)):
	# 	start_intermediate_time = time.time()
	# 	#select = '''select * from quakes order by rand() limit 1 '''
	# 	#stmt = ibm_db.prepare(db, select)
	# 	cursor.execute("select TOP 1 * from all_month order by rand()")
	# 	end_intermediate_time = time.time()
	# 	intermediate_time = end_intermediate_time - start_intermediate_time
	# 	list_of_times.append(intermediate_time)
	# end_time = time.time()
	# time_taken = (end_time - start_time) / int(query_limit)
	#time_taken=89
	#list_of_times=[10,20,30]
	return render_template('test.html',xaxis=json.dumps(xaxis),yaxis=json.dumps(yaxis))

if __name__ == '__main__':
    app.run()
