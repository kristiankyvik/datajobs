import feedparser
import jobClassifier
from dateutil.parser import parse
import re




URL = 'http://careers.stackoverflow.com/jobs/feed?searchTerm=data+science'


def getJobs():
	queries = []
	jobs = feedparser.parse(URL)['entries']
	for job in jobs:
		job_url =  job['link']
		job_ref_number = job_url.split('/')[-2]
		print "BEFORE: " + job['title']
		print "AFTER: " + getTitle(job['title'])
		job_title = getTitle(job['title'])
		job_company = job['author']
		job_location = job['location']
		job_description =  job['summary_detail']['value']
		job_language = job['summary_detail']['language']
		job_published = parse(job['published'])

		if 'tags' in job:
			job_tags = [ tag['term'] for tag in job['tags']]

		q = buildQuery(job_ref_number, job_title, job_company, job_location, job_description, job_url, job_language, job_published)
		queries.append(q)
	return queries

def getTitle(full_title):
	if full_title.endswith('(allows remote)'):
	  full_title = full_title[:-15]
	return full_title[0:full_title.rfind('(')].strip()

def buildQuery(ref_num, title, company, location, description, url, language, published):
	query = 'INSERT INTO  job(ref_number, title, company, location, description, url, language, published)' + 'VALUES (?, ?, ?, ?, ?, ?, ?, ?);'
	params = (ref_num, title, company, location, description, url, language, published)
	q = [query, params]
	return q



