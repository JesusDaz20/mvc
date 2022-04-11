import web 
import mvc.firebase_config as token
import pyrebase
import app 
import json

render = web.template.render("mvc/views/public/")
class Usuarios:
    def GET(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            users = db.child("usuarios").get()
            return render.usuarios(users) 
            except Exception as error:
                print("Error Usuarios.GET: {}".format(error))
                return render.usuarios(message) 

        