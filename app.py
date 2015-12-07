import sqlite3
from flask import Flask,render_template
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


app.debug = True

@app.route('/')

def index():
	data = { "count": 3}
	return render_template("index.html", data=data )

if __name__ == '__main__':

  db = sqlite3.connect(app.config['DATABASE'])

  stored_jobs = [int(item[0]) for item in db.execute('SELECT ref_number FROM job;')]
  print stored_jobs
  queries = getJobs()
  for query in queries:
    print query[1][0]
    if int(query[1][0]) not in stored_jobs:
      db.execute(query[0], query[1])
  db.commit()
  db.close()
  print 'comitted'

  app.run(debug=True, use_reloader=False)

