import feedparser

url = 'http://careers.stackoverflow.com/jobs/feed?searchTerm=data+science'
feed = feedparser.parse(url)


jobs = feed['entries']

job = jobs[0]

count = 0
for job in jobs:
	job_url =  job['link']
	job_id = job_url.split('/')[-2]
	job_title = job['title']
	job_company = job['author']
	job_location = job['location']
	job_description =  job['summary_detail']['value']
	job_language = job['summary_detail']['language']

	if 'tags' in job:
		job_tags = [ tag['term'] for tag in job['tags']]
	job_published = job['published']

	count = count + 1
	if count > 1:
		break




	print job_title
	print job_company
	print job_location
	print job_description

	print job_language
	print job_url
	print job_id
	print job_tags
	print job_published
	print
	print
