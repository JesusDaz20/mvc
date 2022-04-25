import web 
import mvc.firebase_config as token
import pyrebase
import app 

render = web.template.render("mvc/views/admin/")
class Usuarios:
    def GET(self):
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            users = db.child("usuarios").get()
            print(users)
            return render.usuarios(users) 

            

 