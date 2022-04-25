import web 
import mvc.firebase_config as token
import pyrebase
import app 
import json

render = web.template.render("mvc/views/admin/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()
class Agregar_sucursal:
    def GET(self):
        message = None
        localId = web.cookies().get('localId')
        all_users = db.child("Sucursales").get() 
        sucursales = db.child("Sucursales").child(localId).get()
        return render.agregar_sucursal(sucursales)
           
    def POST(self):  
         try:
            formulario = web.input()
            name = formulario.name
            enfriamiento1 = formulario.enfriamiento1
            Humedad = formulario.Humedad
            Temperatura = formulario.Temperatura
            Humedad2 = formulario.Humedad2
            Temperatura2 = formulario.Temperatura2
            sucursales = db.child("Sucursales").child(name).get()

            datos_sucursales = {'enfriamiento1': enfriamiento1, 'Producto1':{"Humedad":"Humedad","Temperatura":"Temperatura"},'Producto2':{"Humedad":"Humedad","Temperatura":"Temperatura"} } 
            result = db.child("Sucursales").child(name).update(datos_sucursales)
            return web.seeother('/agregar_sucursal') 
         except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error agregar_sucursal.POST: {}".format(message)) 
            return render.agregar_sucursal(sucursales)  


            

 