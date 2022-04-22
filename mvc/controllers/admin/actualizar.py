import web 
import mvc.firebase_config as token
import pyrebase
import json
import app

render = web.template.render("mvc/views/admin/")


class Actualizar: 
    def GET(self, localId):
        localId = web.cookies().get('localId')
        all_users = db.child("usuarios").get() 
        user = db.child("usuarios").child(localId).get()
        return render.actualizar(user)

    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            formulario = web.input()
            name = formulario.name
            phone = formulario.phone
            email = formulario.email
            password= formulario.password
            level = formulario.level
            status = formulario.status
            datos_usuarios = {'name': name,'phone': phone,'email':email, 'level':level, 'status':status} 
            result = db.child("usuarios").child(id).update(datos_usuarios)
            print(result)
            return web.seeother('/usuarios') 
        except Exception as error:
            print("Error actualizar.POST: {}".format(message)) 
            return web.seeother('/usuarios')  
