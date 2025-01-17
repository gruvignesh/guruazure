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
	range1 = int(request.args['range'])
	#lowmag = request.args['lowdep']
	#highermag = request.args['higherdep']
	#longitude=request.args['Longitude']
	x=[]
	y=[]
	for temp in range(0,range1):
		x.append(temp)
		temp1=(temp*temp*temp)%10
		y.append(temp1)
		my_dict = {i: y.count(i) for i in y}

	z=[]
	for j in my_dict:
		z.append(my_dict[j])

	#sql='select StateName from voting11 where TotalPop between 2000 and 8000 '
	#sql1='select StateName from voting11 where TotalPop between 8000 and 40000 '
	#cursor.execute(sql)
	#rows = cursor.fetchall()
	#cursor.execute(sql1)
	#rows1 = cursor.fetchall()
	#start_time1 = time.time()
	# for i in range(0, int(query_limit)):
	# 	rngvalue = random.uniform(float(lowmag), float(highermag))
	# 	sql = 'select * from all_month where mag>=? '
	# 	cursor.execute(sql, (rngvalue,))
	#end_time1 = time.time()
	#time_taken = (end_time1 - start_time1) / int(query_limit)
	#return render_template('restricted.html',time_taken=time_taken)
	return render_template('test1.html',xaxis=json.dumps(x),yaxis=json.dumps(z))


@app.route('/barchart', methods=['GET', 'POST'])
def barchart():
	cursor=connection.cursor()
	#query_limit = request.args['chart1']
	population1 = request.args['pop1']
	population2=request.args['pop2']
	population3=request.args['pop3']
	population4=request.args['pop4']
	sql='select count(*),StateName from voting11 where TotalPop between ? and ? group by StateName'
	sql1='select count(*),StateName from voting11 where TotalPop between ? and ? group by StateName'
	cursor.execute(sql,(population1,population2))
	rows = cursor.fetchall()
	cursor.execute(sql,(population3,population4))
	rows1 = cursor.fetchall()
	xaxis=[]
	yaxis=[]
	zaxis=[]
	paxis=[]
	for r in rows:
		xaxis.append(r[0])
		yaxis.append(r[1])
	for r1 in rows1:
		zaxis.append(r1[0])
		paxis.append(r1[1])

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
	return render_template('test.html',xaxis=json.dumps(xaxis),yaxis=json.dumps(yaxis),zaxis=json.dumps(zaxis),paxis=json.dumps(paxis))


@app.route('/piechart', methods=['GET', 'POST'])
def piechart():
	cursor=connection.cursor()
	query_limit = request.args['chart2']
	sql="select place from quake6 where place like '%Texas%' or place like '%CA%'"
	cursor.execute(sql)
	rows = cursor.fetchall()
	xaxis=[]
	yaxis=[]
	for r in rows:
		xaxis.append(r[0].split(',', 1)[-1].strip())
		#yaxis.append(r[1])
	yaxis.append(a.count('Texas'))
	yaxis.append(a.count('CA'))
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
	return render_template('test1.html',xaxis=json.dumps(xaxis),yaxis=json.dumps(yaxis))


if __name__ == '__main__':
    app.run()
