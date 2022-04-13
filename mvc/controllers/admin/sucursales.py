import web 
import mvc.firebase_config as token
import pyrebase
import app 

render = web.template.render("mvc/views/admin/")
class Sucursales:
    def GET(self):
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            return render.sucursales() 

            

 