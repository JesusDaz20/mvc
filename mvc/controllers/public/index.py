import web 
import mvc.firebase_config as token
import pyrebase
import app 
import json

render = web.template.render('mvc/views/public/') 

class Index:
    def GET(self):
        return render.index() 
    def POST(self): 
        return render.index()    
