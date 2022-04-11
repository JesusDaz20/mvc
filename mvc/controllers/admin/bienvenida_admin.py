import web 
import mvc.firebase_config as token
import pyrebase
import app 

render = web.template.render("mvc/views/admin/")

class Bienvenida_admin:
    def GET(self): 
        ("Bienvenida_admin.GET localID: ",web.cookies().get('localId'))
        try: 
            ("Bienvenida_admin.GET localID: ",web.cookies().get('localId')) 
            if web.cookies().get('localId') == "0": 
                return web.seeother("bienvenida_admin") 
            else: 
                return render.bienvenida_admin() 
        except Exception as error: 
            print("Error Bienvenida_admin.GET: {}".format(error))  


