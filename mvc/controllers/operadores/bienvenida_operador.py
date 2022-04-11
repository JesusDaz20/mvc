import web 
import mvc.firebase_config as token
import pyrebase
import app 

render = web.template.render("mvc/views/admin/")

class Bienvenida_operador:
    def GET(self): 
        ("Bienvenida_operador.GET localID: ",web.cookies().get('localId'))
        try: 
            ("Bienvenida_operador.GET localID: ",web.cookies().get('localId')) 
            if web.cookies().get('localId') == "0": 
                return web.seeother("bienvenida_operador") 
            else: 
                return render.bienvenida_operador() 
        except Exception as error: 
            print("Error Bienvenida_operador.GET: {}".format(error))  