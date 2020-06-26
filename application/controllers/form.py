import web
import app
render = web.template.render('application/views/')
class Form:
   def GET(self):
       print("entrando a metdo form")
       return  render.formulario()


