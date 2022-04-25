import web 
import mvc.firebase_config as token
import pyrebase
import app 

render = web.template.render("mvc/views/admin/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()
class Borrar_sucursal:
    def GET(self):
        all_users = db.child("Sucursales").get() 
        return render.borrar_sucursal()
           
    def POST(self):  
         formulario = web.input()
         name = formulario.name
         db.child("Sucursales").child(name).remove()
        
         return render.borrar_sucursal()  

