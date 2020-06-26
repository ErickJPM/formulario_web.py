import web
import app
import json
render = web.template.render('application/views/')
class FormVista:
    def GET(self):
        form=web.input()
        matricula=form['matricula']
        nombre=form['nombre']
        apellido1=form['priapellido']
        apellido2=form['segapellido']
        edad=form['edad']
        fecnac=form['born']
        sexo=form['genero']
        estado=form['estado']
        print(matricula)
        print(nombre)
        print(apellido1)
        print(apellido2)
        print(edad)
        print(fecnac)
        print(sexo)
        print(estado)
        if(matricula=="" or nombre=="" or apellido1=="" or apellido2=="" or edad=="" or fecnac=="" or sexo=="null" or estado=="null"):
            result={}
            result['status']="Faltan valores"
            return json.dumps(result)
        else:
            return  render.vistas(matricula,nombre,apellido1,apellido2,edad,fecnac,sexo,estado)
        
            
        


