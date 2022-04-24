import web 
import mvc.firebase_config as token
import pyrebase
import json
import app

render = web.template.render("mvc/views/admin/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()


class Actualizar: 
    def GET(self):
        localId = web.cookies().get('localId')
        all_users = db.child("usuarios").get() 
        user = db.child("usuarios").child(localId).get()
        return render.actualizar(user)

    def POST(self):
        formulario = web.input()
        id = formulario.id
        name = formulario.name
        phone = formulario.phone
        level = formulario.level
        status = formulario.status
        datos_usuarios = {'name': name,'phone': phone, 'level':level, 'status':status} 
        result = db.child("usuarios").child(id).update(datos_usuarios)
        print(result)
        return web.seeother('/usuarios') 
       