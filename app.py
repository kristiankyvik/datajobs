import sqlite3
import schedule
import time
from flask import Flask,render_template, jsonify
from contextlib import closing
from stackOverflowFeed import getJobs

# dbconfiguration
DATABASE = 'tmp/datajobs.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'


app = Flask(__name__)
app.config.from_object(__name__)

db = sqlite3.connect(app.config['DATABASE'])

app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data')
def data():
    return jsonify({'data': query_db('SELECT title, company, location, url, published FROM job;')})

def query_db(query, args=(), one=False):
  print 'running query'
  db = sqlite3.connect(app.config['DATABASE'])
  cur = db.cursor()
  cur.execute(query, args)

  r = [dict((cur.description[i][0], value) \
             for i, value in enumerate(row)) for row in cur.fetchall()]
  cur.connection.close()
  db.close()
  return (r[0] if r else None) if one else r

def addNewJobs():
  db = sqlite3.connect(app.config['DATABASE'])
  stored_jobs = [int(item[0]) for item in db.execute('SELECT ref_number FROM job;')]
  new_jobs = getJobs()
  jobs_added = 0
  for job in new_jobs:
    if int(job[1][0]) not in stored_jobs:
      #print "adding " + job[1][1] + " to the database"
      db.execute(job[0], job[1])
      jobs_added += 1
  db.commit()
  db.close()
  print str(jobs_added) + ' jobs added'

if __name__ == '__main__':
  addNewJobs()
  schedule.every(30).minutes.do(addNewJobs)
  app.run(debug=True, use_reloader=False)

  while True:
    schedule.run_pending()
    time.sleep(1)




