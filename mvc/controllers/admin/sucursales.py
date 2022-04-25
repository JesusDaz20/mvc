import web 
import mvc.firebase_config as token
import pyrebase
import app 

render = web.template.render("mvc/views/admin/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()
class Sucursales:
    def GET(self):
        status_1 = db.child("Sucursales").child("sucursal1").child("enfriamiento1").get()
        status_2 = db.child("Sucursales").child("sucursal2").child("enfriamiento2").get()
        return render.sucursales(status_1, status_2)
           
    def POST(self):  
         localId = web.cookies().get('localId')
         formulario = web.input()
         enfriamiento1 = formulario.enfriamiento1
         enfriamiento2 = formulario.enfriamiento2
         db.child("Sucursales").child("sucursal1").update({"enfriamiento1": enfriamiento1})
         db.child("Sucursales").child("sucursal2").update({"enfriamiento2": enfriamiento2})
         status_1 = db.child("Sucursales").child("sucursal1").child("enfriamiento1").get()
         status_2 = db.child("Sucursales").child("sucursal2").child("enfriamiento2").get()
         return render.sucursales(status_1, status_2)  


            

 