import web 
import mvc.controllers.public.firebase_config as token
import pyrebase
import app 
import json

app = web.application(urls, globals())
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
            web.setcookie('localIdd', user['localId']) 
            print("localId:",web.cookies().get('localId')) 
            localId = user['localId'] 
            return web.seeother('/bienvenida')
        except Exception as error: 
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error login.POST: {}".format(message)) 
            return render.login(message) 