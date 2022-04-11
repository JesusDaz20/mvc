import app
import web
import mvc.firebase_config as token
import pyrebase

index = web.application(urls, globals()) 
render = web.template.render('mvc/views/public/') 

class Index:
    def GET(self):
        return render.index() 

