import os
import sys
import web
import json
import smtplib

urls = ('/.*', 'hooks')

app = web.application(urls, globals())

class hooks:
    def GET(self):
		return "Hello, world!"

    def POST(self):
	
		payload = json.loads(web.data())

		#os.system("git pull origin master")


		#commit_url = payload["push"]["changes"][0]["commits"][0]["links"]["html"]["href"]
		#commit_author = payload["push"]["changes"][0]["commits"][0]["author"]["raw"]["href"]

		DIR = '/home/tarun/'
		author = payload["actor"]["display_name"]
		username = payload["actor"]["username"]
		profile = payload["actor"]["links"]["html"]["href"]

		committed_on = payload["push"]["changes"][0]["new"]["type"]
		branch_name = payload["push"]["changes"][0]["new"]["name"]
		commit_url = payload["push"]["changes"][0]["new"]["target"]["links"]["html"]["href"]
		commit_msg = payload["push"]["changes"][0]["commits"][0]["message"]

		repository_name = payload["repository"]["full_name"]
		repository = repository_name.split('/')
		repo = repository[1]


		os.system('cd '+DIR+repo)
		
		if branch_name == 'master':
			os.system('cd '+DIR+repo+' && git pull origin master')

		#print payload
		#file = open('web.log','w')
		#file.write(payload)
		#file.close()

			
		
		SERVER = "localhost"
		FROM = "tarun.mukherjee@indusnet.co.in"
		TO = ["tarun.mukherjee@indusnet.co.in"]
		SUBJECT = "Hello!"
		TEXT = payload["push"]["changes"][0]["commits"][0]["links"]["html"]["href"]
		message = '%s <%s> just made some changes on %s %s titled %s. To view the detailed change please head over to %s. \n Regards, %s' % (author,username,branch_name, committed_on, commit_msg, commit_url, author)

		server = smtplib.SMTP(SERVER)
		server.sendmail(FROM, TO, message)
		server.quit()
	

	        return 'OK'

if __name__ == '__main__':
    app.run()