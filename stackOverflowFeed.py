import feedparser
import jobClassifier
from dateutil.parser import parse



URL = 'http://careers.stackoverflow.com/jobs/feed?searchTerm=data+science'
queries = []

def getJobs():
	jobs = feedparser.parse(URL)['entries']
	count = 0
	for job in jobs:
		job_url =  job['link']
		job_ref_number = job_url.split('/')[-2]
		job_title = job['title']
		job_company = job['author']
		job_location = job['location']
		job_description =  job['summary_detail']['value']
		job_language = job['summary_detail']['language']
		job_published = parse(job['published'])

		if 'tags' in job:
			job_tags = [ tag['term'] for tag in job['tags']]

		buildQuery(job_ref_number, job_title, job_company, job_location, job_description, job_url, job_language, job_published)
		count = count + 1
		if count > 40:
			return queries


def buildQuery(ref_num, title, company, location, description, url, language, published):
	query = 'INSERT INTO  job(ref_number, title, company, location, description, url, language, published)' + 'VALUES (?, ?, ?, ?, ?, ?, ?, ?);'
	params = (ref_num, title, company, location, description, url, language, published)
	q = [query, params]
	queries.append(q)




