import web 
import mvc.firebase_config as token
import pyrebase
import app 
import json

render = web.template.render("mvc/views/admin/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()
class Actualizar_sucursal:
    def GET(self):
        message = None
        all_users = db.child("Sucursales").get() 
        return render.actualizar_sucursal()
           
    def POST(self):  
         try:
            formulario = web.input()
            name = formulario.name
            enfriamiento1 = formulario.enfriamiento1
            Humedad = formulario.Humedad
            Temperatura = formulario.Temperatura
            Humedad2 = formulario.Humedad2
            Temperatura2 = formulario.Temperatura2
            db.child("Sucursales").child(name).get()

            datos_sucursales = {'enfriamiento1': "", 'Producto1':{"Humedad":Humedad,"Temperatura":Temperatura},'Producto2':{"Humedad2":Humedad2,"Temperatura2":Temperatura2} } 
            result = db.child("Sucursales").child(name).update(datos_sucursales)
            return web.seeother('/actualizar_sucursal') 
         except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error actualizar_sucursal.POST: {}".format(message)) 
            return render.actualizar_sucursal()  
