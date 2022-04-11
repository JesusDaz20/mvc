import web 
import mvc.firebase_config as token
import pyrebase
import app 
import json

render = web.template.render("mvc/views/public/") 


class Login: 
    def GET(self):
        message = None
        return render.login(message) 

    def POST(self):
        try:
            message = None
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            formulario = web.input() 
            email = formulario.email 
            password= formulario.password
            user = auth.sign_in_with_email_and_password(email, password)
            cookie= auth.get.account_info(user['localId'])
            localId=user['localId']
            web.setcookie('localIdd', user['localId'])
            all_users = db.child("usuarios").get() 
            for user in all_users.each():
                if user.key() == localId and user.val()['level'] == "admin":
                    if user.val()['status'] == 'true':
                        return web.seeother('/bienvenida_admin') 
                    else:
                        admin = user.val()['level'] == "admin"
                        return web.seeother('/logout')
                elif user.key() == localId and user.val()['level'] == "operador":
                    if user.val()['status'] == 'true':
                        return web.seeother('/bienvenida_operador') 
                    else:
                        admin = user.val()['level'] == "admin"
                        return web.seeother('/logout')
        except Exception as error: 
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error login.POST: {}".format(message)) 
            return render.login(message) 