import web 
import mvc.firebase_config as token
import pyrebase
import json
import app

render = web.template.render("mvc/views/admin/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() 
db = firebase.database()


class Estado: 
    def GET(self):
        localId = web.cookies().get('localId')
        all_users = db.child("usuarios").get()
        user = db.child("usuarios").child(localId).get() 
        return render.estado(user)

    def POST(self):
        formulario = web.input()
        id = formulario.id
        status = formulario.status
        datos_usuarios = {'status':status} 
        result = db.child("usuarios").child(id).update(datos_usuarios)
        
        all_users = db.child("usuarios").get()
        for user in all_users.each():
            usuario=user.key()
            status= user.val()['status']
            level= user.val()['level']
            if (id == "kRfouxRGPjbrFkg1kNuHJDx1SLh1" and level=="admin"):
                return render.estado(user)
                break
        else: 
            user = db.child("usuarios").child(localId).get()
        return web.seeother('/usuarios') 
       