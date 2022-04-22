import web 
import mvc.firebase_config as token
import pyrebase
import app 

render = web.template.render("mvc/views/operadores/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()

class Bienvenida_operador:
    def GET(self): 
        localId = web.cookies().get('localId')
        name = db.child("usuarios").child(localId).get()
        return render.bienvenida_operador(name)
           

