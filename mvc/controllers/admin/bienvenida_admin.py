import web 
import mvc.firebase_config as token
import pyrebase
import app 

render = web.template.render("mvc/views/admin/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()

class Bienvenida_admin:
    def GET(self): 
        localId = web.cookies().get('localId')
        name = db.child("usuarios").child(localId).get()
        return render.bienvenida_admin(name)
           