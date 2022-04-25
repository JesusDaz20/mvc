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
        status_1 = db.child("Sucursales").child("sucursal1").child("enfriamiento1").get()
        status_2 = db.child("Sucursales").child("sucursal2").child("enfriamiento2").get()
        return render.bienvenida_operador(name,status_1, status_2)

    def POST(self):  
         formulario = web.input()
         enfriamiento1 = formulario.enfriamiento1
         enfriamiento2 = formulario.enfriamiento2
         db.child("Sucursales").child("sucursal1").update({"enfriamiento1": enfriamiento1})
         db.child("Sucursales").child("sucursal2").update({"enfriamiento2": enfriamiento2})
         status_1 = db.child("Sucursales").child("sucursal1").child("enfriamiento1").get()
         status_2 = db.child("Sucursales").child("sucursal2").child("enfriamiento2").get()
         name = db.child("usuarios").child(localId).get()
         return render.bienvenida_operador(name,status_1, status_2) 
